import sys, re

# part 1
f = open('input.txt', 'r');
inpt = f.read().split(',');
f.close();

def move(m):
    if (m == 'n'):
        return (0,2);
    elif (m == 's'):
        return (0,-2);
    elif (m == 'ne'):
        return (1,1);
    elif (m == 'nw'):
        return (-1,1);
    elif (m == 'sw'):
        return (-1,-1);
    elif (m == 'se'):
        return (1,-1);

p = (0,0);
visited = { (0,0) : True };

for m in inpt:
    mv = move(m);
    p = (p[0] + mv[0], p[1] + mv[1]);
    if (not p in visited):
        visited[p] = True

map = {}

possibleMoves = ['n','s','ne','nw','sw','se'];

def bfs(map, step, queue, dest):
    nextMoves = []

    for pp in queue:
        if (not pp in map):
            map[pp] = step
            if (pp == dest):
                print ('', step, pp)
                return step
            else:
                for m in possibleMoves:
                    mv = move(m);
                    nextMoves.append((pp[0] + mv[0], pp[1] + mv[1]))

    if (len(nextMoves) > 0):
        return bfs(map, step + 1, nextMoves, dest)

print('Part 1: ' + str(bfs(map, 0, [(0,0)], p)))


mapb = {}

def bfs2(map, step, queue, possibilities):
    nextMoves = []

    for pp in queue:
        if (not pp in map):
            map[pp] = step
            if (pp in possibilities):
                possibilities.pop(pp);

            for m in possibleMoves:
                mv = move(m);
                nextMoves.append((pp[0] + mv[0], pp[1] + mv[1]))

    if (len(possibilities) < 1):
        return (map, step + 1, [], possibilities)

    if (len(nextMoves) > 0):
        return (map, step, nextMoves, possibilities)


p2inpt = (mapb, 0, [(0,0)], visited)
while (len(p2inpt[2]) > 0):
    p2inpt = bfs2(p2inpt[0],p2inpt[1],p2inpt[2],p2inpt[3])

print ('Part 2: ' + str(p2inpt[1]))