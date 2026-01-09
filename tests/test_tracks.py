import pytest
import os
import json
from unittest.mock import patch, MagicMock

# Import necessary functions - assuming we will refactor main.py to expose these or make them testable
# We might need to mock os.listdir and other things if we don't want to rely on the real file system too much,
# but using tmp_path is better for integration-like tests.

import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# We will need to import these after we modify main.py.
# For now, I'm writing the test assuming the functions will exist.
from main import get_tracks, get_stats, get_due_card


@pytest.fixture
def mock_questions_dir(tmp_path):
    """Creates a temporary questions directory structure."""
    db_dir = tmp_path / "database"
    db_dir.mkdir()

    # Track 1: Diagnostics (with info.json)
    diag_dir = db_dir / "diagnostics"
    diag_dir.mkdir()
    (diag_dir / "info.json").write_text(
        json.dumps(
            {
                "id": "diagnostics",
                "name": "Diagnostika a testování",
                "description": "Test description",
            }
        )
    )
    (diag_dir / "q1.md").write_text("---\nid: q1\n---\nQuestion 1")

    # Track 2: Math (no info.json)
    math_dir = db_dir / "math"
    math_dir.mkdir()
    (math_dir / "q2.md").write_text("---\nid: q2\n---\nQuestion 2")

    # Global template (should be ignored by get_tracks but present in root)
    (db_dir / "_template.md").write_text("Template")

    return db_dir


def test_get_tracks(mock_questions_dir):
    """Test discovering tracks and reading metadata."""
    # We need to patch QUESTIONS_DIR in main to point to our mock dir
    with patch("main.QUESTIONS_DIR", str(mock_questions_dir)):
        tracks = get_tracks()

        # Sort by id to ensure order
        tracks.sort(key=lambda t: t["id"])

        assert len(tracks) == 2

        # Check Diagnostics
        assert tracks[0]["id"] == "diagnostics"
        assert tracks[0]["name"] == "Diagnostika a testování"
        # Verify path (should be absolute or relative correctly)
        assert tracks[0]["path"].endswith("diagnostics")

        # Check Math (fallback)
        assert tracks[1]["id"] == "math"
        assert tracks[1]["name"] == "math"  # Fallback to dir name
        assert tracks[1]["path"].endswith("math")


def test_get_stats_for_track(mock_questions_dir):
    with patch("main.QUESTIONS_DIR", str(mock_questions_dir)):
        tracks = get_tracks()
        diag_track = next(t for t in tracks if t["id"] == "diagnostics")

        # Pass the specific track directory
        stats = get_stats({}, diag_track["path"])

        # Should have 1 question (score 0 -> "New")
        assert stats["New"] == 1
        assert sum(stats.values()) == 1


def test_get_due_card_for_track(mock_questions_dir):
    with patch("main.QUESTIONS_DIR", str(mock_questions_dir)):
        tracks = get_tracks()
        diag_track = next(t for t in tracks if t["id"] == "diagnostics")
        math_track = next(t for t in tracks if t["id"] == "math")

        # Get card from Diagnostics
        card = get_due_card({}, diag_track["path"])
        assert card is not None
        assert card["id"] == "q1"

        # Get card from Math
        card_math = get_due_card({}, math_track["path"])
        assert card_math is not None
        assert card_math["id"] == "q2"
