import matplotlib.pyplot as plt 
import os

def genseq(a, b, m, seed=1, num=20):
    x = seed % m
    res = []
    for _ in range(num):
        x = (a*x + b)%m
        res.append(x/float(m))
    return res

a = 1229
b = 0
m = 2048
x0 = 123
numpts = 4196

seq = genseq(a, b, m, x0, numpts+1)

plt.scatter(seq[:-1], seq[1:], 1)
plt.xlabel('$u_i$')
plt.ylabel('$u_{i+1}$')
plt.tight_layout()
plt.savefig(os.path.join('output', 'q3out0.png'))
plt.show()
