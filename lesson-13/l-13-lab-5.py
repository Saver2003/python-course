coordinates = {
'border_x': 12,
'border_y': 6,
'house_x': 12,
'house_y': 4
}

print(coordinates['house_x'])
print(coordinates['house_y'])

if coordinates['house_x'] < coordinates['border_x'] and coordinates['house_y'] > coordinates['border_y']:
    print("NW")
elif coordinates['house_x'] > coordinates['border_x'] and coordinates['house_y'] > coordinates['border_y']:
    print("NE")
elif coordinates['house_x'] > coordinates['border_x'] and coordinates['house_y'] < coordinates['border_y']:
    print("SE")
elif coordinates['house_x'] < coordinates['border_x'] and coordinates['house_y'] < coordinates['border_y']:
    print("SW")
elif coordinates['house_x'] == coordinates['border_x'] or coordinates['house_y'] == coordinates['border_y']:
    print("Border")