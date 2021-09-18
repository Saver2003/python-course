from random import randint

num1 = randint(1, 9)
num2 = randint(1, 9)

result = int(input("How much is %s * %s ? " % (num1, num2)))

if num1 * num2 == result:
    print("Correct")
else:
    print("Wrong. Correct answer is: %s" % result)