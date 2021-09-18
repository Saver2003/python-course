import math

marks = {}

print("Enter mark for Bill:")

marks['Bill'] = int(input())

print("Enter mark for Jane:")

marks['Jane'] = int(input())

print("Enter mark for John:")

marks['John'] = int(input())

print("Enter mark for Mary:")

marks['Mary'] = int(input())

result = 0

for i in marks:
    result += marks[i]    

result = result / len(marks)

print("Average mark: %s" % math.ceil(result))