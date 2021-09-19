from random import random, randint

array1 = []
array2 = []
array3 = []

# print(array3)

def arrayFilling(arr):
    if arr == array1:
        for i in range(10):
            r = int(input("Random num %s for array A: " % (i + 1)))
            arr.append(r)
    else:
        for i in range(10):
            r = int(input("Random num %s for array B: " % (i + 1)))
            arr.append(r)





arrayFilling(array1)
arrayFilling(array2)

for i in range(10):
    array3.append(array1[i] + array2[i]) 


# array3 = array1 + array2



print("Array A: %s" % array1)
print("Array B: %s" % array2)
print("Array C: %s" % (array3))
maximum = max(array3)
print("Max: %s" % maximum)