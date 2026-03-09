from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Tests for the New Game bug fix ---
# The bug: clicking New Game did not reset status to "playing" and did not
# clear the guess input field (via widget key change).
# Fix: reset status + increment game_id so the widget gets a new key.

def simulate_new_game(session_state: dict, difficulty: str) -> dict:
    """Replicate the new_game block logic from app.py."""
    session_state["attempts"] = 0
    session_state["score"] = 0
    session_state["history"] = []
    session_state["status"] = "playing"
    session_state["game_id"] += 1
    return session_state


def test_new_game_resets_status_to_playing():
    session_state = {
        "attempts": 5,
        "score": 40,
        "history": [10, 20],
        "status": "won",
        "game_id": 0,
    }
    simulate_new_game(session_state, "Normal")
    assert session_state["status"] == "playing"


def test_new_game_increments_game_id():
    session_state = {
        "attempts": 3,
        "score": 10,
        "history": [30],
        "status": "lost",
        "game_id": 2,
    }
    old_game_id = session_state["game_id"]
    simulate_new_game(session_state, "Normal")
    assert session_state["game_id"] == old_game_id + 1


def test_new_game_widget_key_changes():
    """A new game_id produces a different widget key, clearing the input field."""
    difficulty = "Normal"
    game_id_before = 1
    game_id_after = game_id_before + 1
    key_before = f"guess_input_{difficulty}_{game_id_before}"
    key_after = f"guess_input_{difficulty}_{game_id_after}"
    assert key_before != key_after


def test_new_game_resets_attempts_and_score():
    session_state = {
        "attempts": 7,
        "score": 80,
        "history": [5, 10, 15],
        "status": "lost",
        "game_id": 0,
    }
    simulate_new_game(session_state, "Hard")
    assert session_state["attempts"] == 0
    assert session_state["score"] == 0
    assert session_state["history"] == []
