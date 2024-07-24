from unittest import mock

from app.rps_game import RPSGame


def test_determine_winner_first_player():
    game = RPSGame(
        {"name_1": "Chibi", "move_1": "Rock", "name_2": "Gidget", "move_2": "Scissors"}
    )
    result = game._determine_winner()
    assert result == "player_1"


def test_determine_winner_second_player():
    game = RPSGame(
        {"name_1": "Chibi", "move_1": "Rock", "name_2": "Gidget", "move_2": "Paper"}
    )
    result = game._determine_winner()
    assert result == "player_2"


def test_determine_winner_tie():
    game = RPSGame(
        {
            "name_1": "Chibi",
            "move_1": "Scissors",
            "name_2": "Gidget",
            "move_2": "Scissors",
        }
    )
    result = game._determine_winner()
    assert result == None
