from random import randint

num = randint(1000, 10000)

arr = str(num)
print(arr)
for char in arr:
    print(char)

string = list(arr)
print(string)

for i in string:
    print(i)