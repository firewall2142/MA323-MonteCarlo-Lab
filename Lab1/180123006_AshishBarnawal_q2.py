from matplotlib import pyplot as plt
import sys
import os

def genseq(a, b, m, seed=1, num=20):
	x = seed % m
	res = []
	for _ in range(num):
		res.append(x/float(m))
		x = (a*x + b)%m
	return res

sample_size = int(2e6)
m = 244944
b = 1


# 5 different x0, a=1597, 51749
ind = 0
txtind = 0
x0vals = [1, 11, 42, 101, 121]
avals = [1597, 51749]

for a in avals:
	res = []
	for x0 in x0vals:
		ind += 1
		seq = genseq(a, b, m, x0, sample_size)
		hist_data, bin_edges, _ = plt.hist(seq, range=[0, 1], bins=int(1/0.05), rwidth=0.8)
		res.append(hist_data)
		plt.xlabel('range')
		plt.ylabel('frequency')
		plt.title(f'$x_0 = {x0},\\/a = {a},\\/b={b},\\/m={m}$')
		plt.tight_layout()
		plt.savefig(os.path.join('output', f'q2o{ind}.png'))
		plt.clf()

	with open(os.path.join('output', f'q2a{a}.csv'), 'w') as fp:
		fp.write("$x_0$,")
		fp.write(','.join(list(map(lambda x: str(int(x)), x0vals))))
		fp.write('\n')

		for itr in range(len(bin_edges) - 1):
			fp.write(f"{bin_edges[itr]:.2f}-{bin_edges[itr+1]:.2f},")
			row = ','.join([str(int(res[i][itr])) for i in range(len(x0vals))])
			fp.write(row)
			fp.write('\n')