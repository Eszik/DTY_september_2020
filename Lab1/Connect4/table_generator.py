import random


def generate_table():
    prio = [i % 7 + 1 for i in range(6*7)]
    random.shuffle(prio)
    tableau = [[j for j in range(6)] for i in range(7)]
    for i in range(7):
        for j in range(6):
            tableau[i][j] = prio.pop()
    return tableau
