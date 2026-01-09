import pytest
import os
import json
import shutil
import hashlib
from unittest.mock import patch, MagicMock
# Import the module effectively.
# Since main.py has code that runs on import (ui.page, etc), we might want to be careful.
# But nicegui is usually okay to import if we don't call ui.run().
# However, global variables like QUESTIONS_DIR are there.

import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import functions to test
from main import (
    get_user_hash,
    load_progress,
    save_progress,
    get_progress_file,
    USERS_DIR,
)


@pytest.fixture
def mock_users_dir(tmp_path):
    """Fixture to create a temporary users directory and patch USERS_DIR."""
    # We need to patch the global USERS_DIR in main.py
    # Since we imported specific functions, we might need to patch where they are defined OR used.
    # The functions use the global USERS_DIR.

    test_users_dir = tmp_path / "users"
    test_users_dir.mkdir()

    with patch("main.USERS_DIR", str(test_users_dir)):
        yield test_users_dir


def test_hashing():
    """Verify that hashing is consistent."""
    p1 = "password123"
    h1 = get_user_hash(p1)

    # Check consistency
    assert h1 == get_user_hash(p1)

    # Check correctness (sha256 of password123)
    expected = hashlib.sha256(p1.encode()).hexdigest()
    assert h1 == expected

    # Check difference
    assert h1 != get_user_hash("password124")


def test_load_save_progress(mock_users_dir):
    """Verify loading and saving progress for a user."""
    user_pass = "testuser"
    user_hash = get_user_hash(user_pass)

    # 1. Load non-existent
    prog = load_progress(user_hash)
    assert prog == {}

    # 2. Save data
    data = {"q1": {"score": 10}}
    save_progress(user_hash, data)

    # 3. Check file existence
    expected_file = mock_users_dir / f"{user_hash}.json"
    assert expected_file.exists()

    # 4. Load again
    loaded_prog = load_progress(user_hash)
    assert loaded_prog == data


def test_independent_users(mock_users_dir):
    """Verify that two users have separate progress files."""
    user1 = "alice"
    user2 = "bob"
    h1 = get_user_hash(user1)
    h2 = get_user_hash(user2)

    # Save user 1
    save_progress(h1, {"alice_q": {"score": 10}})

    # Check user 2 is empty
    assert load_progress(h2) == {}

    # Save user 2
    save_progress(h2, {"bob_q": {"score": 20}})

    # Check user 1 is unchanged
    assert load_progress(h1) == {"alice_q": {"score": 10}}

    # Verify files
    assert (mock_users_dir / f"{h1}.json").exists()
    assert (mock_users_dir / f"{h2}.json").exists()


def test_questions_dir_interaction():
    """
    Optional: Test interaction with questions directory if necessary.
    But implementing logic tests is sufficient for now.
    """
    pass
