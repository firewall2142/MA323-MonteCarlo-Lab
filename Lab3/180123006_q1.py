from random import random
import matplotlib.pyplot as plt

nums = list(range(1, 9999+1, 2))
N = len(nums)
sample_size = 1000000

results = []
for _ in range(sample_size):
    # since probabilites are same
    # so q_i = i/N, we need to find largest i
    # s.t. u < q_i = i/N, or u*N < q_i
    u = random()
    ind = int(u*N)
    results.append(nums[ind])

plt.title(f'samples = {sample_size}')
plt.xlabel('generated value')
plt.ylabel('probability')
plt.hist(results, bins = 100, density=True)
# uncomment the below line to save the image
#plt.savefig('q1.png')
plt.show()
