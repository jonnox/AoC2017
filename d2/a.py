import sys
# part 1
f = open('input.txt', 'r');

totaldiff = 0

for line in f:
    nums = line.split();
    max = -sys.maxint - 1
    min = sys.maxint
    for ns in nums:
        n = int(ns)
        if (n > max):
            max = n
        if (n < min):
            min = n
    totaldiff = totaldiff + (max - min)

f.close()

print totaldiff;

#part 2

f = open('input.txt', 'r');

totaldiff = 0

for line in f:
    nums = line.split();
    inums = list(map(lambda num: int(num), nums))
    inums.sort(reverse=True)
    l = len(inums)
    for i in range(l-1):
        for j in range(i+1,l):
            if (inums[i] % inums[j] == 0):
                totaldiff = totaldiff + (inums[i] / inums[j])
                break

print totaldiff
