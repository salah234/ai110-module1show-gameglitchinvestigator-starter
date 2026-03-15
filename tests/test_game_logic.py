import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess
import pytest
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


# --- Win edge cases ---

def test_win_at_boundary_low():
    # Smallest possible secret (Easy mode lower bound)
    result = check_guess(1, 1)
    assert result[0] == "Win"

def test_win_at_boundary_high():
    # Largest possible secret (Hard mode upper bound)
    result = check_guess(300, 300)
    assert result[0] == "Win"

def test_win_string_secret():
    # Glitch mechanic: even attempts convert secret to a string.
    # check_guess must still detect a correct guess when secret is "50".
    result = check_guess(50, "50")
    assert result[0] == "Win"


# --- Too High edge cases ---

def test_too_high_by_one():
    # One above secret — smallest possible "Too High"
    result = check_guess(51, 50)
    assert result[0] == "Too High"

def test_too_high_string_secret():
    # Glitch mechanic: guess is higher than a string secret
    result = check_guess(60, "50")
    assert result[0] == "Too High"

def test_too_high_large_range():
    # Hard mode range (1–300): guess well above secret
    result = check_guess(299, 150)
    assert result[0] == "Too High"


# --- Too Low edge cases ---

def test_too_low_by_one():
    # One below secret — smallest possible "Too Low"
    result = check_guess(49, 50)
    assert result[0] == "Too Low"

def test_too_low_string_secret():
    # Glitch mechanic: guess is lower than a string secret
    result = check_guess(40, "50")
    assert result[0] == "Too Low"

def test_too_low_large_range():
    # Hard mode range (1–300): guess well below secret
    result = check_guess(1, 150)
    assert result[0] == "Too Low"

def test_too_low_guess_zero():
    # Guess of 0 is below any valid secret (range starts at 1)
    result = check_guess(0, 1)
    assert result[0] == "Too Low"

def test_too_low_negative_guess():
    # Negative guess should always be "Too Low"
    result = check_guess(-5, 50)
    assert result[0] == "Too Low"
