from score.Frame import Frame 
from score.Player import Player

player = Player()

player.play(10)
player.play(10)
player.play(10)
player.play(10)
player.play(10)
player.play(10)
player.play(10)
player.play(10)
player.play(10)
player.play(10)
player.play(10)
player.play(10)


frames = player.get_frames()
i = 1
for frame in frames:
    print(f"Frame {i}: roll scores = {frame.get_roll_scores()} | bonus = {frame.bonus}")
    i += 1
print(player.score)