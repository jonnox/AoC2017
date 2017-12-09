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
      print "End of file"
      break

    if (not isSkip):
        if (c == '!'):
            isSkip = True
        elif (isGarbage):
            if (c == '>'):
                isGarbage = False
            else:
                cleared = cleared + 1
        else:
            if (c == '<'):
                isGarbage = True
            elif (c == '{'):
                l = l + 1 # increase level
            elif (c == '}'):
                score = score + l
                l = l - 1 # decrease level

    else:
        isSkip = False


f.close();

print('Part 1: ' + str(score));
print('Part 2: ' + str(cleared));