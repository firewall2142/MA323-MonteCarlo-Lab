

from random import random
import scipy.special as sc
import matplotlib.pyplot as plt
import numpy as np

# number of elements to generate
list_N = [1000, 100000]


a1 = 5
a2 = 2

# values for alpha1 and alpha2
values_list = [ (2.0, 2.0), (1, 1.25), (1.25, 1), (2.0, 1.0), (1.25, 3.2)]


for a1, a2 in values_list:
    def f(x):
        return ((x**(a1-1))*((1-x)**(a2-1)))/sc.beta(a1, a2)

    x_minima = (a1 - 1)/(a1 + a2 - 2)
    c = f(x_minima)
    print(f'For a1, a2 = {a1}, {a2}:\t x* = {x_minima}\tc = {c}')

    def generate():
        while True:
            u1, u2 = random(), random()
            if c*u2 <= f(u1):
                return u1
    
    for N in list_N:
        results = [generate() for _ in range(N)]
        _, bins, _ = plt.hist(results, density=True, bins=100)
        plt.xlabel('x')
        plt.ylabel('density')
        plt.title(f'$\\alpha_1$ = {a1}, $\\alpha_2$ = {a2}, sample size={N}')
        plt.plot(bins, f(bins), 'k-', label='f(x)', )
        plt.legend()
        plt.savefig(f'result_{a1:.2f}_{a2:.2f}_{N}.png')
#         plt.show()
        plt.clf()
