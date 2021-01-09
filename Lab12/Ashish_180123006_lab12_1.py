##########################################
# Copyleft  © 2020 Ashish Kumar Barnawal #
##########################################

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('grayscale')

# radical inverse function
def radinv(n, base=2):
	ans = 0
	p = 1.0/base
	while n > 0:
		ans += (n%base)*p
		n = n//base
		p = p/base
	return ans

def lcg(size, a=1237, c=1, m=2**16, seed=12345):
    ans = [0]*size
    xi = seed
    for i in range(size):
        xn = (a*xi + c) % m
        xi = xn
        ans[i] = float(xn)/m
    return np.array(ans)


print('ans =',  radinv(2, 2) - radinv(2, 3))

N = 1000
plt.subplot(121)
plt.title('Van der Corput Sequence')
plt.xlabel('$x_i$')
plt.ylabel('$x_{i+1}$')

values = [radinv(i, 2) for i in range(1, N+1)]
plt.scatter(values[:-1], values[1:], s=1, c='black')


plt.subplot(122)
plt.title('LCG\na=1237 m=$2^{16}$\nc=1, seed=12345')
plt.xlabel('$x_i$')
plt.ylabel('$x_{i+1}$')

lcg_values = lcg(N)
plt.scatter(lcg_values[:-1], lcg_values[1:], s=1, c='black')

plt.tight_layout()
plt.savefig('xivsxi1.png')
plt.show()
plt.clf()



plotid = 1
for N in [100, 100000]:
	values = [radinv(i, 2) for i in range(1, N+1)]
	lcg_values = lcg(N)

	plt.subplot(220 + plotid)
	plotid+=1
	plt.title(f'Van der Corput\nN={N}')
	plt.xlabel('t')
	plt.ylabel('P(X<t)')
	plt.hist(values, bins=100, density=True, cumulative=True)


	plt.subplot(220 + plotid)
	plotid+=1
	plt.title(f'LCG\nN={N}')
	plt.xlabel('t')
	plt.ylabel('P(X<t)')
	plt.hist(lcg_values, bins=100, density=True, cumulative=True)

plt.tight_layout()
plt.savefig('cdf.png')
plt.show()

