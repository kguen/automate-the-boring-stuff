import sys, openpyxl

wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb[wb.sheetnames[0]]

for col in range(1, sheet.max_column+1):
    newFile = open(f'column_{col}.txt', 'w')
    for row in range(1, sheet.max_row+1):
        cellValue = sheet.cell(row=row, column=col).value
        if cellValue != None:
            newFile.write(cellValue)
    newFile.close()