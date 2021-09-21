symbol = '*'
height = int(input("Input pyramid height: "))
array = []

for i in range(height):
    array.append(' ')
for i in range(height):
    array.pop()
    string = ''.join(array)
    if i == 0:
        symbol = '*'
    else:
        symbol += '**'
    print(string, symbol, string)
