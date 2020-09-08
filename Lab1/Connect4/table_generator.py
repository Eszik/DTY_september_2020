import random
import numpy as np


def generate_table():
    prio = [i % 15 + 1 for i in range(6*7)]
    random.shuffle(prio)
    tableau = [[j for j in range(6)] for i in range(7)]
    for i in range(7):
        for j in range(6):
            tableau[i][j] = prio.pop()
    return tableau

def gaussian_table(sigma, mu):
    import numpy as np
    x, y = np.abs(np.linspace(-3,3,7)), np.abs(np.linspace(-2.5,2.5,6))
    d = np.array([x,]*6).transpose() + np.array([y,]*7)
    g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
    return g

print(gaussian_table(4.8, 0))