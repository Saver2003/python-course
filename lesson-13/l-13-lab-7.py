radius = [12, 35, 4]

pi = 3.14
area_arr = []

def roundArea(radius):
    for i in radius:
        area_arr.append(pi * (i ** 2))

roundArea(radius)

print(area_arr)