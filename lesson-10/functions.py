a = input()
b = input()
operation = input()

print(a + b)

if operation == "+":
    result = int(a) + int(b)
    print("Result of addition is %s" % (result))
elif operation == "-":
    result = a - b
    print("Result of subtraction is %s" % (result))
else:
    print("There is no such operation")
