import random

def generate_table():
    sum = 6*7
    tableau = [[0 for j in range(6)] for i in range(7)]
    for i in range(7):
        for j in range(6):
            r = random.random()*sum
            tableau[i][j] = r
            sum -= r
    return tableau
