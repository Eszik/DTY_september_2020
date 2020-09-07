from table_generator import gaussian_table
from game import Game
from ai_player import AIPlayer

def GPlayer(sigma, mu):
  return AIPlayer(gaussian_table(sigma, mu))

players = [GPlayer(i//10,0) for i in range(45,56)]
scores = [0]*10

for (i, player1) in enumerate(players):
  for (j, player2) in enumerate(players):
    if i == j:
      pass
    game = Game(player1, player2, 7, 6, 4, verbose=False)
    result = game.run()
    if result == 1:
      scores[i] += 1
    elif result == -1:
      scores[j] += 1
    else:
      scores[i] += 0.5
      scores[j] += 0.5

best_score = 0
best_player = 0

print(scores)