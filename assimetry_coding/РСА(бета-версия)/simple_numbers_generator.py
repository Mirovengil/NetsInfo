filename = input('FILENAME: ')
MAX = int(input('MAX ACCEPTABLE SIMPLE NUMBER: '))
file = open('./' + filename + '.txt', 'w')
mass = list(range(2, MAX))
i = 2
while i <= MAX:
    j = i + i
    while j <= MAX:
        if mass.count(j) > 0:
            mass.remove(j)
        j = j + i
    i = i + 1
for i in mass:
    file.write(str(i) + '\n')
file.close()
