import numpy as np
import matplotlib.pyplot as plt
import os
plt.style.use('ggplot')

def X(U):
    return 0.5 - 0.5*np.cos(U*np.pi)

def F(X):
    return (2/np.pi)*np.arcsin(np.sqrt(X))

sample_list = [100, 500, 1000, 5000, 10000, 100000]

res = [] # tuple storing calculated (mean,var)
for N in sample_list:

    sample = X(np.random.random(N))

    freq, intervals = np.histogram(sample , bins=np.linspace(0, 1, 50))
    vals = freq/float(N)
    midpts = (intervals[:-1] + intervals[1:])/2.0
    cdf = np.array([np.count_nonzero(sample < x) for x in midpts])/N

    plt.plot(midpts, F(midpts), 'k-.', label='expected')
    plt.plot(midpts, cdf, 'b', label='actual')
    plt.xlabel('$t$'); plt.ylabel('$P(X<t)$')
    plt.title(f'num. of samples=${N}$')
    plt.legend(loc='upper left')

    plt.savefig(os.path.join('images', f'q3n{N}.png'))

    res.append((np.mean(sample), np.var(sample)))

    plt.clf()

print('|         |', end='')
for N in sample_list:
    print(f'{N:8d} |', end='')
print('')
for _ in range(len(sample_list) + 1):
    print('+|'[int(_==0)] + '---------', end='')
print('|')

print(f'| mean    |', end='')

for i in range(len(sample_list)):
    print(f'{res[i][0]:9.5f}', '|', end='')
print('')

print(f'|variance |', end='')

for i in range(len(sample_list)):
    print(f'{res[i][1]:9.5f}', '|', end='')
print('\n\n')