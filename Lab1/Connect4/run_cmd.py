import argparse

from game import Game
from player import HumanPlayer, RandomPlayer
from ai_player import AIPlayer
from table_generator import generate_table


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--p1', default='player 1')
    parser.add_argument('--p2', default='player 2')
    parser.add_argument('--rows', default='6', type=int)
    parser.add_argument('--cols', default='7', type=int)
    parser.add_argument('--num', default='4', type=int)
    args = parser.parse_args()




    best_tab = [[1,2,3,3,2,1],[3,4,5,5,4,3],[7,9,11,11,9,7],[9,10,13,13,10,9],[7,9,11,11,9,7],[3,4,5,5,4,3],[1,2,3,3,2,1]]
    tab1 = generate_table()

    player1 = AIPlayer(best_tab)
    player1.name = args.p1

    player2 = AIPlayer(tab1)
    player2.name = args.p2
<<<<<<< HEAD
    game = Game(player1, player2, args.cols, args.rows, args.num, verbose=False)
    game.run()
=======

    for i in range(10):
        game = Game(player1, player2, args.cols, args.rows, args.num, verbose=False)

        if game.run() == 1:
            print(1)
            new_tab = generate_table()
            player2 = AIPlayer(new_tab)
        else:
            print(2)
            best_tab = new_tab
            new_tab = generate_table()
            player1 = AIPlayer(new_tab)
    
    print(best_tab)
            
>>>>>>> d1e04cbf3974877b23c8d623548ab71370da007b
