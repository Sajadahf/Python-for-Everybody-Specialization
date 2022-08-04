# Retrieving lists of Keys and Values
order = {'apples': 10, 'oranges': 15, 'cucamber': 4, 'melon': 9}
print(list(order))
print(order.keys())
print(order.values())
print(order.items())

# Two Iteration Variables
for name,number in order.items():
    print(name, number)
