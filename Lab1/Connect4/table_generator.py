import random
import numpy as np


def generate_table():
<<<<<<< HEAD
    prio = [i % 15 + 1 for i in range(6*7)]
    random.shuffle(prio)
    tableau = [[j for j in range(6)] for i in range(7)]
    for i in range(7):
        for j in range(6):
            tableau[i][j] = prio.pop()
    return tableau
=======
    sum = 6*7
    tableau = np.zeros((7,6))
    for i in range(7):
        for j in range(6):
            r = random.random()*sum
            tableau[i][j] = r
            sum -= r
    np.random.shuffle(tableau)
    return tableau
>>>>>>> a8b0fd55c7e0cb1a8f9e3780ef5d2f69bc12048b
