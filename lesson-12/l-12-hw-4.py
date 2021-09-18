print("Enter numbers:")

numbers = []
total = 0

while True:

    number = input()
    if number == 'end':
        break

    numbers.append(number)

for i in numbers:
    total += int(i)

print(total)

print("You entered: %s" % ', '.join(numbers))
print("Total: %s" % total)
print("Average: %s" % (int(total) / len(numbers)))
