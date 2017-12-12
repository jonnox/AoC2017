import sys, re, ll

# part 1
f = open('input.txt', 'r');
inpt = map(lambda x: int(x), (f.read()).split(','));
f.close();

skip = 0 # skip

start = ll.Node(0);

n = start

inpt = [3,4,1,5]

# create 256 ring
hash = range(5);

l = len(hash)
a = 0
b = 0

for i in inpt:
    if (i > 0):
        b = (a + i - 1)
        for j in range(a,b):
            jm = j % l
            k = (b - (j-a))
            km = k % l
            c = hash[jm] # [ a, ..., b ] store a
            hash[jm] = hash[km]
            hash[km] = c

    print (a,b, hash)
    a = (b + 1 + skip) % l
    skip = skip + 1



print('Part 1: ' + str());
print('Part 2: ' + str());