print("Enter 2 sentences: ")
first_sentence = input()
second_sentence = input()
print(first_sentence)
print(second_sentence)

arr_first = first_sentence.split(' ')
arr_second = second_sentence.split(' ')
arr_equal = []
# print(arr_first)
# print(arr_second)

for i in arr_first:
    for j in arr_second:
        if i == j:
            arr_equal.append(i)

ready_string = ', '.join(arr_equal)
print(f"Similar words are: {ready_string}")
