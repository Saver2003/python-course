a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


arr = [a, b, c]
arr.sort(reverse=True)
max_side = arr[0]

if max_side < arr[1] + arr[2]:
    print('Yes')
else:
    print('No')