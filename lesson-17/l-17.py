f = open('fruit.txt', 'w')
f.write('Apples, 10\n')

f.write('Peaches, 5\n')

f.close()

f = open('fruit.txt', 'a')

f.write('Cherries, 60\n')

f.write('Apricots, 25\n')

f.close()
