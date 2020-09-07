from player import Player
from board import Board
import copy
from copy import deepcopy
import utils


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """
    def heuristique_IA(self,grille,couleur):            #Calcul de la valeur de la grille à l'aide de la grille arbitraire
        valeur =0
        for nume_col,col in enumerate (grille.board) :      
            for nume_row,row in enumerate(col):
                valeur+=row*self.tableau[nume_col][nume_row]    #self.tableau contient les valeurs associées aux cases
        return valeur*couleur

    def getWinner2(self,pos,grille):        #Reformulation de la fonction getWinner du module game
        tests = []
        tests.append(grille.getCol(pos[0]))
        tests.append(grille.getRow(pos[1]))
        tests.append(grille.getDiagonal(True, pos[0] - pos[1]))
        tests.append(grille.getDiagonal(False, pos[0] + pos[1]))
        for test in tests:
            color, size = utils.longest(test)
            if size >= 4:
                return color
        return 0
    
    #elagage alpha beta

    def max_value(self,grille,profondeur,couleur,alpha,beta):
        alpha2=alpha
        if profondeur == 1 :
            return self.heuristique_IA(grille,couleur)
        possible = grille.getPossibleColumns()
        for state in possible:
            copie = copy.deepcopy(grille)
            row = copie.play(couleur,state)
            test = self.getWinner2((state,row),copie)       #si la situation est une fin de partie, on arrête d'explorer
            if test ==couleur :
                return 10000
            m = self.min_value(copie,profondeur-1,couleur,alpha2,beta)
            alpha2=max(alpha2,m)

            if alpha2>=beta:
                return beta
        return alpha2

    def min_value(self,grille,profondeur,couleur,alpha,beta):
        beta2=beta
        if profondeur == 1 :
            return self.heuristique_IA(grille,couleur)
        
        possible = grille.getPossibleColumns()
        for state in possible:
            copie = copy.deepcopy(grille)
            row = copie.play(couleur*-1,state)
            test = self.getWinner2((state,row),copie)       #si la situation est une fin de partie, on arrête d'explorer
            if test ==couleur*-1 :
                return -10000
            m = self.max_value(copie,profondeur-1,couleur,alpha,beta2)
            beta2 = min(beta2,m)
            if alpha>=beta2:
                return beta2
        return beta2

    def elagage(self,grille,profondeur,couleur):
        poss= grille.getPossibleColumns()
        alpha = -40000
        beta = 40000
        col = poss[0]
        for state in poss:
            copie = copy.deepcopy(grille)
            row = copie.play(couleur,state)
            test = self.getWinner2((state,row),copie)
            if test !=0 :
                return state
            else :
                m = self.min_value(copie,profondeur-1,couleur,alpha,beta)
            if m>alpha:
                alpha = m
                col = state
        return col
    
    def __init__(self, tableau):
        super().__init__()
        self.name = "QuadBot"
        self.tableau = tableau     #valeurs arbitraires choisies pour le plateau

    
    def getColumn(self, board):
        couleur = self.color

        col = self.elagage(grille = board , profondeur =5 ,couleur = couleur,)
        return col