import sys, re

# part 1
f = open('input.txt', 'r');

l = 0 # level

score = 0
cleared = 0

isGarbage = False
isSkip = False

while True:
    c = f.read(1) # read character by character
    if not c:
      break # End of file

    if (not isSkip):
        if (c == '!'):
            isSkip = True # Start skipping
        elif (isGarbage):
            if (c == '>'):
                isGarbage = False # stop tracking garbage
            else:
                cleared = cleared + 1 # track characters cleared
        else:
            if (c == '<'):
                isGarbage = True # Start tracking garbage
            elif (c == '{'):
                l = l + 1 # increase level
            elif (c == '}'):
                score = score + l
                l = l - 1 # decrease level

    else:
        isSkip = False # complete skipped character


f.close();

print('Part 1: ' + str(score));
print('Part 2: ' + str(cleared));