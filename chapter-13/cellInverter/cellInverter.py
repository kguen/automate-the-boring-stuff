import sys, openpyxl

fileName = sys.argv[1]
# load old workbook
oldWb = openpyxl.load_workbook(fileName)
oldSheet = oldWb[oldWb.sheetnames[0]]
# create new workbook
newWb = openpyxl.Workbook()
newSheet = newWb['Sheet']

for i in range(1, oldSheet.max_row+1):
    for j in range(1, oldSheet.max_column+1):
        newSheet.cell(row=j, column=i).value = oldSheet.cell(row=i, column=j).value

newWb.save('inverted.xlsx')