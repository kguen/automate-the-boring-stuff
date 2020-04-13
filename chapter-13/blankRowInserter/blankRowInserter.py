import sys, openpyxl

startFrom = int(sys.argv[1])
numOfLines = int(sys.argv[2])
fileName = sys.argv[3]

wb = openpyxl.load_workbook(fileName)
sheet = wb[wb.sheetnames[0]]

# for every row needs to be moved starting from last row
for i in range(sheet.max_row, startFrom - 1, -1):
    # for every cell in that row
    for j in range(1, sheet.max_column + 1):
        # move every cell down numOfLines row 
        sheet.cell(row=i+numOfLines, column=j).value = sheet.cell(row=i, column=j).value
        sheet.cell(row=i, column=j).value = None

wb.save('rowsInserted.xlsx')