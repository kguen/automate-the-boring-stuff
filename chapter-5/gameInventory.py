def displayInventory(inventory):
    totalItem = 0
    print('Inventory:')
    for key, value in inventory.items():
        totalItem += value
        print(str(value) + ' ' + key)
    print('Total number of items: ' + str(totalItem))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inventory, dragonLoot)
displayInventory(inventory)