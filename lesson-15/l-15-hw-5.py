
# pif = int(input("введите любое число от 1 до 9: "))

# for i in range(1, pif+1):
#     print(*range(i, i*pif+1, i), sep='\t')
num = int(input("Enter number: "))
num_len = len(str(num))
max_width = len(str(num ** 2))

print("%s" % (max_width * " "), end="|")
for i in range(1, num + 1):
    print((str(i)).rjust(max_width * 2), end="")
print()

print("%s%s%s" % (("-" * (num_len + 1)), "+", (max_width * 2 * num * "-")))

for i in range(1, num + 1):
    print((str(i)).ljust(len(str(num)) + 1), end="|")
    for j in range(1, num + 1):
        print(str((i * j)).rjust(max_width * 2), end="")
    print()
