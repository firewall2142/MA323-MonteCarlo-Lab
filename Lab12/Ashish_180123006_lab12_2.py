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


for N in [100, 100000]:
	values_x = [radinv(i, 2) for i in range(1, N+1)]
	values_y = [radinv(i, 3) for i in range(1, N+1)]
	
	size = [1, 0.05][int(N>1000)]
	plt.scatter(values_x, values_y, s=size, c='black')
	plt.title(f'Halton N={N}')
	plt.xlabel('$\\phi_2(i)$')
	plt.ylabel('$\\phi_3(i)$')
	plt.savefig(f'halton{N}.png')
	plt.show()
