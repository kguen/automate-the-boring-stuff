import sys, openpyxl

textFiles = sys.argv[1:]
wb = openpyxl.Workbook()
sheet = wb['Sheet']

for col, fileName in enumerate(textFiles, start=1):
    file = open(fileName)
    lines = file.readlines()
    for row, line in enumerate(lines, start=1):
        sheet.cell(row=row, column=col).value = line

wb.save('result.xlsx')