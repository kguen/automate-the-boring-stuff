def commaCode(spam):
    retStr = ''
    for index, item in enumerate(spam):
        if index == len(spam) - 1:
            retStr += 'and ' + str(item)
        else:
            retStr += str(item) + ', '
    return retStr

print(commaCode(['apples', 'bananas', 'tofu', 'cats']))
print(commaCode([1, '2', 3, '4']))
print(commaCode([]))