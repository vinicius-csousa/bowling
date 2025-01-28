from src.score.BowlingManager import BowlingManager
from src.score.Player import Player
from src.score.Frame import Frame
from src.score.enums.GameStatus import GameStatus
from src.helpers.helpers import calculate_cumulative_scores


def test_mixed_game():
    manager = BowlingManager([Player("test_player")])

    rolls = [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]
    expected_scores = [
        5,
        14,
        29,
        49,
        60,
        61,
        77,
        97,
        117,
        133,
    ]  # Scores expected according to the coding challenge pdf

    for roll in rolls:
        manager.play(roll)

    assert manager.calculate_player_score() == 133

    cumulative_scores = calculate_cumulative_scores(manager.players[0])

    for score, expected_score in zip(cumulative_scores, expected_scores):
        assert score == expected_score


def test_perfect_game():
    manager = BowlingManager([Player("test_player")])

    i = 0
    while i < 12:
        manager.play(10)
        i += 1

    assert manager.calculate_player_score() == 300
    assert manager.players[0].game_status == GameStatus.PERFECT_GAME


def test_gutter_game():
    manager = BowlingManager([Player("test_player")])

    i = 0
    while i < 20:
        manager.play(0)
        i += 1

    assert manager.calculate_player_score() == 0
    assert manager.players[0].game_status == GameStatus.GUTTER_GAME
