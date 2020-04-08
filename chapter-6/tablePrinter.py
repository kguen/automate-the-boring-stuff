def printTable(table):
    rows = len(table)
    cols = len(table[0])

    for i in range(rows):
        maxLen = 0 # Length of longest string in this row
        for j in range(cols):
            itemLen = len(table[i][j])
            if maxLen < itemLen:
                maxLen = itemLen
        
        # Justify strings based on length of longest string in each row
        for j in range(cols):
            table[i][j] = table[i][j].rjust(maxLen)
    
    # Printing
    for j in range(cols):
        for i in range(rows):
            print(table[i][j], end=' ')
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)