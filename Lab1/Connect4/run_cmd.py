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


    dicc = {}
    best_tab = [[1,2,3,3,2,1],[3,4,5,5,4,3],[7,9,11,11,9,7],[9,10,13,13,10,9],[7,9,11,11,9,7],[3,4,5,5,4,3],[1,2,3,3,2,1]]
    
    nb_players = 5

    with open("fights.txt", "a") as log:

        player = AIPlayer(best_tab)
        player.name = "champion"
        dicc[player.name] = { "victoires" : 0, "player": player }

        log.write("\nPlayer : " + player.name)
        log.write("\n" + str(best_tab))

        for players in range(nb_players):
            tab = generate_table()

            player = AIPlayer(tab)
            player.name = "player" + str(players)
            dicc[player.name] = { "victoires" : 0, "player" : player }

            log.write("\n\nPlayer : " + player.name)
            log.write("\n" + str(tab))

        print("total combats : " + str(nb_players * nb_players / 2))

        num_combat = 1
        for i in range(nb_players):
            for j in range(i + 1, nb_players):
                print("combat " + str(num_combat))
                num_combat += 1
                player1_dicc = dicc[list(dicc.keys())[i]]
                player2_dicc = dicc[list(dicc.keys())[j]]
                player1 = player1_dicc["player"]
                player2 = player2_dicc["player"]
                
                log.write("\n\nFight : " + player1.name + " VS " + player2.name)

                game = Game(player1, player2, args.cols, args.rows, args.num, verbose=False)
                result = game.run()

                if result == 1:
                    log.write("\n\t Result : " + player1.name)
                    player1_dicc["victoires"] +=1
                elif result == -1:
                    log.write("\n\t Result : " + player2.name)
                    player2_dicc["victoires"] +=1
        print("ecriture")
        log.write("\n\nScore : ")
        max_score = 0
        best_player = None
        for i in range(nb_players):
            player_dicc = dicc[list(dicc.keys())[i]]
            if player_dicc["victoires"] > max_score:
                max_score = player_dicc["victoires"]
                best_player = player_dicc["player"]
            player_dicc = dicc[list(dicc.keys())[i]]
            log.write("\n\t" + list(dicc.keys())[i] + " : " + str(player_dicc["victoires"]))

        print("Winner : " + best_player.name)
        log.write("\n\nBest player : " + best_player.name)
            
