import sys
import os


def genseq(a, b, m, seed=1, num=20):
	x = seed % m
	res = []
	for _ in range(num):
			res.append(x)
			x = (a*x + b)%m
	return res

seq_size = 14

a = 6; b = 0; m = 11
res1 = []
for x0 in range(m):
	seq = genseq(a, b, m, x0, seq_size)
	res1.append(seq)

with open(os.path.join('output', 'q1o1.csv'), 'w') as fp:
	output = "$x0$\n"

	for x0 in range(m):
		output += f'{x0},'
		output += ','.join(list(map(str, res1[x0])))
		output += '\n'
	fp.write(output)

a=3
res2 = []
for x0 in range(m):
	seq = genseq(a, b, m, x0, seq_size)
	res2.append(seq)

with open(os.path.join('output', 'q1o2.csv'), 'w') as fp:
	output = "$x0$\n"

	for x0 in range(m):
		output += f'{x0},'
		output += ','.join(list(map(str, res2[x0])))
		output += '\n'
	fp.write(output)