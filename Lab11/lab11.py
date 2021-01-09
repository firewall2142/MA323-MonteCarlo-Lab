import numpy as np

# N = number of values to generate
def uniform(size, a=22695477, c=1, m=2**32, seed=12345):
    ans = [0]*size
    xi = seed
    for i in range(size):
        xn = (a*xi + c) % m
        xi = xn
        ans[i] = float(xn)/m
    return np.array(ans)


n = 10000

print(f'n = {n}')
print('\n N\t|     D\n-----------------------')

xs = uniform(n)
for N in [10, 20, 50, 100]:
    A, vol = np.linspace(start=0, stop=1, num=N+1, retstep=True)
    D = 0
    for i in range(N):
        numele = np.sum(np.logical_and(xs >= A[i], xs < A[i+1]))
        d = abs(float(numele)/n - vol)
        D = max(d, D)

    print(N, '\t|', D)
