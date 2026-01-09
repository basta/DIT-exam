import os
import json
import hashlib
import getpass

QUESTIONS_DIR = "./database"
USERS_DIR = "./users"
OLD_PROGRESS_FILE = "progress.json"


def get_user_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def migrate():
    if not os.path.exists(OLD_PROGRESS_FILE):
        print(f"No {OLD_PROGRESS_FILE} found. Nothing to migrate.")
        return

    print("--- DIT Exam Progress Migration ---")
    print(
        "This script will migrate your existing progress to the new multi-user system."
    )

    password = getpass.getpass(
        prompt="Enter your passkey (to associate with existing progress): "
    )
    if not password:
        print("Passkey cannot be empty.")
        return

    user_hash = get_user_hash(password)
    new_file = os.path.join(USERS_DIR, f"{user_hash}.json")

    if os.path.exists(new_file):
        print(f"Warning: A profile for this passkey already exists at {new_file}.")
        confirm = input("Overwrite? (y/N): ")
        if confirm.lower() != "y":
            print("Migration aborted.")
            return

    # Load old data
    try:
        with open(OLD_PROGRESS_FILE, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {OLD_PROGRESS_FILE}: {e}")
        return

    # Ensure users directory exists
    os.makedirs(USERS_DIR, exist_ok=True)

    # Write new data
    try:
        with open(new_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Successfully migrated progress to {new_file}")
        print(f"User Hash: {user_hash}")

        # Optional: Rename old file
        # os.rename(OLD_PROGRESS_FILE, OLD_PROGRESS_FILE + ".bak")
        # print(f"Renamed {OLD_PROGRESS_FILE} to {OLD_PROGRESS_FILE}.bak")

    except Exception as e:
        print(f"Error writing new file: {e}")


if __name__ == "__main__":
    migrate()
