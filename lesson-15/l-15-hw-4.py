items = ['Milk', 'Bread', 'Cheese', 'Chocolate', 'Water']
prices = [10, 5, 20.5, 7.15, 2.99]

print('{:<20}{:<20}'.format('Name', 'Price'))
for i in range(len(items)):
    print('{:<20}{:<20}'.format(items[i], prices[i]))
