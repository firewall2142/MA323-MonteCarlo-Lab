import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use('ggplot')

#linear congruence generator
def lcg(n, a, b, m, seed):
    x = seed%m
    result = []
    for _ in range(n):
        result.append(float(x)/m)
        x = (a*x + b)%m
    return result

def fib_gen(n):
    #generate the first 17 values
    U = lcg(17, 5, 1, 2**12, 1)

    #generate the remaining values
    for i in range(17, n):
        U.append(U[i-17] - U[i-5])
        if(U[i] < 0):
            U[i] = U[i]+1  
    return U


for n in [1000, 10000, 100000]:
    U = fib_gen(n)

    plt.scatter(U[:-1], U[1:], s=2)
    plt.title(f'$n={n}$')
    plt.xlabel('$U_i$')
    plt.ylabel('$U_{i+1}$')
    plt.savefig(os.path.join('images',f'q1n{n}a.png'))
    plt.clf()

    plt.hist(U, bins=30, rwidth=0.8)
    plt.title(f'$n={n}$')
    plt.ylabel(f'Frequency')
    plt.xlabel('$U$')
    plt.savefig(os.path.join('images',f'q1n{n}b.png'))
    plt.clf()
