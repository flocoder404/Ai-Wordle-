import unittest
from wordle import WordleGame
import pytest

class TestWordleInitialization(unittest.TestCase):

  def test_init_sets_empty_strings():
    game = WordleGame()
    assert game.target == ""
    assert game.guess == ""

  def test_set_target_valid():
    game = WordleGame()
    game.set_target("hello") 
    assert game.target == "hello"

  def test_set_target_invalid_length(): 
    game = WordleGame()
    with pytest.raises(ValueError):
      game.set_target("hi")
 
  def test_check_guess_all_match():
    game = WordleGame()
    game.set_target("hello")
    game.set_guess("hello")
    assert game.check_guess() == "22222"

if __name__ == '__main__':
  unittest.main()