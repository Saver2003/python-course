import random

day_numbers = int(input("Enter number of days: "))
print()

exchange1 = []
exchange2 = []
exchange3 = []


def random_num(nums, array):
    for i in range(nums):
        num = random.uniform(65.0, 70.0)
        # array.append("{0:.2f}".format(num))
        array.append(num)


random_num(day_numbers, exchange1)
random_num(day_numbers, exchange2)
random_num(day_numbers, exchange3)

print("Generated prices: ")
print(exchange1)
print(exchange2)
print(exchange3, '\n')

course = exchange1 + exchange2 + exchange3
sum = 0
for i in course:
    sum += i
average = sum / len(course)

print("Average price: {0:.5f}".format(average))
