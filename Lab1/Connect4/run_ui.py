import argparse

from player import HumanPlayer, RandomPlayer
from ai_player import AIPlayer
from ui_game import UIGame

from ai_player import AIPlayer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--p1', default='player 1')
    parser.add_argument('--p2', default='player 2')
    args = parser.parse_args()


    player1 = AIPlayer([[7, 4, 5, 5, 4, 2], [4, 6, 6, 4, 3, 5], [5, 3, 2, 2, 6, 1], [5, 7, 7, 2, 6, 4], [3, 1, 4, 2, 2, 7], [5, 1, 7, 6, 1, 1], [3, 6, 3, 3, 1, 7]])
    player1.name = args.p1
    player2 = AIPlayer([[1,2,3,3,2,1],[3,4,5,5,4,3],[7,9,11,11,9,7],[9,10,13,13,10,9],[7,9,11,11,9,7],[3,4,5,5,4,3],[1,2,3,3,2,1]] )
    player2.name = args.p2

    game = UIGame(player1, player2)
    print(game)

