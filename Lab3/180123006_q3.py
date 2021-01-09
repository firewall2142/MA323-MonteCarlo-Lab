import matplotlib.pyplot as plt
import numpy as np
from random import randint, random

# sample size
N = 1000000

# minimum value of c is 1.2
c = 1.5


probab = [0.11, 0.12, 0.09, 0.08, 0.12, 0.10, 0.09, 0.09, 0.10, 0.10]
nums = [1,2,3,4,5,6,7,8,9,10]


def generate(_c):
    itr = 0  # number of iterations
    while True:
        itr += 1
        x = randint(1, 10)  # discrete uniform dist
        u = random()        # U[0,1]
        
        # f(x) is probab[x-1], g(x) = 1/10 = 0.1
        if u <= probab[x-1]/(_c*0.1) :
            return x, itr
    


sample = [generate(c) for _ in range(N)]
avgitr = sum(list(map(lambda x: x[1], sample)))/N
sample = np.array(list(map(lambda x: x[0], sample)))
counts = [0]*10

for x in nums:
    counts[x-1] = np.count_nonzero(sample == x)
counts = np.array(counts)/N
    
plt.bar(nums, counts)
plt.xlabel('t')
plt.ylabel('P(X=t)')
plt.title(f'num samples = {N}')
# uncomment this line and set the path to store image
plt.savefig('lab3/images/q3.png')
plt.show()

mxdiff = np.abs(np.array(counts) - np.array(probab)).max()
print(f'max|P(X=t) - f(t)| = {mxdiff}')
print(f'avg iterations = {avgitr}')
