from score.Player import Player
from score.BowlingManager import BowlingManager

manager = BowlingManager([Player('Vinicius')])

manager.play(1)
manager.play(4)
print(manager.calculate_player_score(0))

manager.play(4)
manager.play(5)
print(manager.calculate_player_score(0))

manager.play(6)
manager.play(4)

manager.play(5)
manager.play(5)
print(manager.calculate_player_score(0))

manager.play(10)

manager.play(0)
print(manager.calculate_player_score(0))
manager.play(1)
print(manager.calculate_player_score(0))

manager.play(7)
manager.play(3)
print(manager.calculate_player_score(0))

manager.play(6)
manager.play(4)
print(manager.calculate_player_score(0))

manager.play(10)
print(manager.calculate_player_score(0))

manager.play(2)
manager.play(8)
print(manager.calculate_player_score(0))

manager.play(6)
print(manager.calculate_player_score(0))

frames = manager.players[0].get_frames()
i = 1
for frame in frames:
    print(f"Frame {i}: roll scores = {frame.get_roll_scores()} | bonus = {frame.bonus} | total score = {frame.calculate_score()} | status = {frame.status}")
    i += 1
print(manager.calculate_player_score(0))


#print("\n")
#frames = manager.players[1].get_frames()
#i = 1
#for frame in frames:
#    print(f"Frame {i}: roll scores = {frame.get_roll_scores()} | bonus = {frame.bonus} | total score = {frame.calculate_score()} | status = {frame.status}")
#    i += 1

