import numpy as np 
import matplotlib.pyplot as plt
import os
plt.style.use('ggplot')

def X(U, theta):
    return -theta*np.log(1-U)
def F(x, theta):
    return 1 - np.exp(-x/theta)

sample_list  =  [100, 1000, 10000, 100000]
theta_list = [5.0, 9.0]

for theta in theta_list:
    
    res = [] # tuple storing calculated (mean,var)

    for N in sample_list:
        sample = X(np.random.random(N), theta)

        intervals = np.linspace(0, 30.0, 11)
        midpts = (intervals[:-1] + intervals[1:])/2.0
        cdf = np.array([np.count_nonzero(sample < x) for x in midpts])/N

        plt.plot(midpts, F(midpts, theta), 'k-.', label='expected')
        plt.plot(midpts, cdf, 'b', label='actual')
        plt.xlabel('$t$'); plt.ylabel('$P(x<t)$')
        plt.title(f'$\\theta$={theta}\tsamples=${N}$')
        plt.legend(loc='upper left')
        # plt.show()
        plt.savefig(os.path.join('images', f'q2n{N}t{int(theta)}.png'))

        res.append((np.mean(sample), np.var(sample)))

        # print(f'\n$\\theta$={theta} samples=${N}$')
        # print('|         | expected |   actual   |')
        # print('|---------+----------+------------|')
        # print('|mean     |' + f'{theta: 10.2f}|' + f'{np.mean(sample): 12.8f}|')
        # print('|variance |' + f'{theta**2: 10.2f}|' + f'{np.var(sample): 12.8f}|')
        # # print(f'variance: expected={theta**2:6.2f}, actual={np.var(sample): 8.5f}')
        plt.clf()
    
    print(f'theta = {theta}')
    print('|         | expected|', end='')
    for N in sample_list:
        print(f'{N:8d} |', end='')
    print('')
    for _ in range(len(sample_list) + 2):
        print('+|'[int(_==0)] + '---------', end='')
    print('|')

    print(f'| mean    | {theta:8.4f}|', end='')

    for i in range(len(sample_list)):
        print(f'{res[i][0]:8.4f}', '|', end='')
    print('')


    print(f'|variance | {theta**2: 8.4f}|', end='')

    for i in range(len(sample_list)):
        print(f'{res[i][1]:8.4f}', '|', end='')
    print('\n\n')