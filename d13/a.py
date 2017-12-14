import sys, re

# part 1
f = open('input.txt', 'r');

cost = 0

fwa = []

for line in f:
    ids = re.findall('(\w+)', line)

    level = int(ids[0])
    depth = int(ids[1])
    pos = (level) % (depth * 2 - 2)

    fwa.append((level,depth * 2 - 2))

    if (pos == 0):
        cost = cost + (level * depth)

f.close()

print('Part 1: ' + str(cost))

i = 0
failed = True

while(failed):
    i = i + 1
    failed = False
    for w in fwa:
        if ((w[0] + i) % w[1] == 0):
            failed = True
            break

print('Part 2: ' + str(i))

