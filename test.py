__author__ = 'yi-linghwong'

a = [[1,2,3], [5,6,3], [7,8,9]]
b = []
temp = []

for x in a:
    if x[2] not in temp:
        b.append(x)
        temp.append(x[2])

print (b)
print (temp)

