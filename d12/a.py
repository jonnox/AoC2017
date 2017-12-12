import sys, re

# part 1
f = open('input.txt', 'r');

links = {}
uids = []

def attachLink(links, prmy, id):
    if (not id in links):
        links[id] = {
            'l': {},
            'visited': False
        }
    if (not prmy in links):
        links[prmy] = {
            'l': {},
            'visited': False
        }

    if (not id in links[prmy]['l']):
        links[prmy]['l'][id] = True
    if (not id in links[id]['l']):
        links[id]['l'][prmy] = True



for line in f:
    ids = re.findall('(\w+)', line)
    uids.append(ids[0]);
    prmy = ids[0]; # primary link
    for id in ids[1:]:
        attachLink(links,prmy,id);

f.close();

def visit(links, n):
    if (links[n]['visited']):
        return (False, []);
    else:
        links[n]['visited'] = True
        return (True, list(links[n]['l'].keys()))

groups = 0
for uid in uids:
    if (not links[uid]['visited']):
        groups = groups + 1
        tovisit = [uid];
        visited = 0;

        while (len(tovisit) > 0):
            tv = []
            for n in tovisit:
                result = visit(links, n)
                if (result[0]):
                    visited = visited + 1
                    tv = tv + result[1]
            tovisit = tv

        if (uid == '0'):
            print ('Part 1: ' + str(visited))

print ('Part 2: ' + str(groups))