import sys
# part 1

s = 1;
n = 1;
i = 368078;
# i = 12

while (n < i):
	s = s + 2;
	n = s * s;

mid = (s-1) / 2 #midpoint
#distance to midpoint
step = n - i;
dmid = abs(mid - (step % s))
print mid + dmid

#part 2

def calcval(g,p):
	val = g[p[0] - 1][p[1] + 1]
	val = val + g[p[0]][p[1] + 1]
	val = val + g[p[0] + 1][p[1] + 1]
	val = val + g[p[0] - 1][p[1]]
	val = val + g[p[0] + 1][p[1]]
	val = val + g[p[0] - 1][p[1] - 1]
	val = val + g[p[0]][p[1] - 1]
	val = val + g[p[0] + 1][p[1] - 1]

	return val

g = [[0 for x in range(s+1)] for y in range(s+1)]

g[mid][mid] = 1

pos = (mid + 1,mid)


v = 1

m = 0

while (v < i):
	v = calcval(g,pos)
	g[pos[0]][pos[1]] = v
	if (m == 0): # up
		if (g[pos[0] - 1][pos[1]] != 0):
			pos = (pos[0],pos[1] + 1)
		elif (g[pos[0]][pos[1] - 1] == 0):
			m = 1
			pos = (pos[0], pos[1] - 1)
		else:
			pos = (pos[0] - 1, pos[1])
	elif (m == 1): # left
		if (g[pos[0] + 1][pos[1]] == 0):
			m = 2
			pos = (pos[0] + 1, pos[1])
		else:
			pos = (pos[0], pos[1] - 1)
	elif (m == 2): # down
		if (g[pos[0]][pos[1] + 1] == 0):
                        m = 3
                        pos = (pos[0], pos[1] + 1)
                else:
                        pos = (pos[0] + 1, pos[1])
	else: # right
		if (g[pos[0] - 1][pos[1]] == 0):
                        m = 0
                        pos = (pos[0] - 1, pos[1])
                else:
                        pos = (pos[0], pos[1] + 1)

print v
