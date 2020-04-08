import pyinputplus as pyip

# Ingredient prices
bread = {'wheat': 1.0, 'white': 1.5, 'sourdough': 2.5}
protein = {'chicken': 4.0, 'turkey': 6.5, 'ham': 5.0, 'tofu': 2.5}
cheese = {'cheddar': 1.0, 'mozzarella': 1.5, 'swiss': 2.5}
additional = 0.2
totalPrice = 0.0

# Bread
response = pyip.inputMenu(list(bread.keys()))
totalPrice += bread[response.lower()]
# Protein
response = pyip.inputMenu(list(protein.keys()))
totalPrice += protein[response.lower()]
# Cheese
response = pyip.inputYesNo('Do you want cheese?\n')
if response == 'yes':
    response = pyip.inputMenu(list(cheese.keys()))
    totalPrice += cheese[response.lower()]
# Mayo
response = pyip.inputYesNo('Do you want mayo?\n')
if response == 'yes':
    totalPrice += additional
# Mustard
response = pyip.inputYesNo('Do you want mustard?\n')
if response == 'yes':
    totalPrice += additional
# Lettuce
response = pyip.inputYesNo('Do you want lettuce?\n')
if response == 'yes':
    totalPrice += additional
# Tomato
response = pyip.inputYesNo('Do you want tomato?\n')
if response == 'yes':
    totalPrice += additional
# Number of sandwiches
response = pyip.inputInt('How many sandwiches do you want?\n', min=1)
totalPrice *= response

print('Total price: %.1f' % totalPrice)