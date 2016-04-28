__author__ = 'yi-linghwong'

lines = open('../output/featimp_normalisation/sgd/politics.csv','r').readlines()
print (lines[:5])

lines1 = []
lines2 = []
lines3 = []

i = 0

for line in lines:
    if line in ['\n', '\r\n']:
        i += 1
        continue

    if i == 1:
        lines1.append(line)

    if i == 2:
        lines2.append(line)

    if i == 3:
        lines3.append(line)

print (lines3)
