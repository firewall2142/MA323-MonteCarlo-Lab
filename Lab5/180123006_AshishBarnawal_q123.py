import numpy as np
from random import random
from math import sin, cos, log, pi, sqrt
import time
import matplotlib.pyplot as plt
plt.style.use('default')


# density functions from the formula
def normal_density(mean, var, x):
    return np.exp(-((x-mean)**2)/(2*var))/np.sqrt(2*np.pi*var)

def box_muller(num_samples):
    start = time.time()
    result = []
    for _ in range(int(num_samples/2)):
        u1, u2 = random(), random()
        R = -2*log(u1)
        v = 2*pi*u2
        rtR = sqrt(R)
        z1 = rtR*cos(v)
        z2 = rtR*sin(v)
        result.append(z1)
        result.append(z2)
    end = time.time()
    print('\n\nBox-Muller\n---------')
    print(f'{num_samples} samples time = {(end-start)*1000:.4f}ms')
    print('\n\n')
    return result

def marsaglia_bray(num_samples):
    start = time.time()
    result = []
    tries = 0
    for _ in range(int(num_samples/2)):
        x = 2
        u1, u2 = -1, -1
        while x > 1:
            tries += 1
            u1, u2 = random(), random()
            u1, u2 = 2*u1 - 1, 2*u2 - 1
            x = u1**2 + u2**2
        y = sqrt(-2*log(x)/x)
        z1, z2 = u1*y, u2*y
        result.append(z1)
        result.append(z2)
    end = time.time()
    print('\n\nMarsaglia-Bray\n---------')
    print(f'{num_samples} samples time = {(end-start)*1000:.4f}ms')
    print(f'fraction of rejects = {(tries-(num_samples/2))/tries}')
    print('\n\n')
    return result


num_samples = 10000
method = marsaglia_bray

for num_samples in [100, 10000]:
    for method in [box_muller, marsaglia_bray]:
        # N(0, 1) distribution
        samples = np.array(method(num_samples))

        bins = np.linspace(-5, 10, 50)
        midpts = (bins[1:]+bins[:-1])/2.0

        # part (a)
        print(f'num samples = {samples.size}')
        print(f'mean        = {samples.mean()}')
        print(f'variance    = {samples.var()}')

        # part (b)
        plt.hist(samples, bins=50)
        plt.ylabel('frequency')
        plt.title(f'sample={samples.size}\n{method.__name__} N(0,1)')
        plt.savefig(f'{method.__name__}_{num_samples}_hist.png')
        plt.tight_layout()
        plt.show()
        plt.clf()

        # part (c)
        # N(0,5) mean=0, variance=5
        samples_n05 = samples*np.sqrt(5)
        samples_n55 = samples_n05 + 5


        cdf_sample_n05 = np.cumsum(np.histogram(samples_n05, bins=bins)[0])/num_samples
        cdf_sample_n55 = np.cumsum(np.histogram(samples_n55, bins=bins)[0])/num_samples

        # N(0, 5)
        plt.title(f'$N(0,5)$, sample={samples_n05.size}\n{method.__name__}')
        plt.plot(bins, normal_density(0, 5, bins), label='formula density')
        plt.plot(bins[1:], cdf_sample_n05, label='sample CDF')
        plt.legend(loc="upper left")
        plt.savefig(f'n05_{method.__name__}_{num_samples}.png')
        plt.show()
        plt.clf()

        plt.title(f'$N(5,5)$, sample={samples_n55.size}\n{method.__name__}')
        plt.plot(bins, normal_density(5, 5, bins), label='formula density')
        plt.plot(bins[1:], cdf_sample_n55, label='sample CDF')
        plt.legend(loc="upper left")
        plt.savefig(f'n55_{method.__name__}_{num_samples}.png')
        plt.show()
        plt.clf()

        
for N in [100, 10000, 100000, 1000000]:
    marsaglia_bray(N)
