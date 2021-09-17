a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
c = int(input("Enter third num: "))


def sumNum(a, b, c):
    return b * (a - c)


result = sumNum(a, b, c)

print("a = %s, b = %s, c = %s, результат = %s" % (a, b, c, result))
