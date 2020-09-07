import random
import numpy as np

def generate_table():
    sum = 6*7
    tableau = np.zeros((7,6))
    for i in range(7):
        for j in range(6):
            r = random.random()*sum
            tableau[i][j] = r
            sum -= r
    np.random.shuffle(tableau)
    return tableau