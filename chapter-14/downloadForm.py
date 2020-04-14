import ezsheets
# Connect to form sheet
ss = ezsheets.Spreadsheet('1opU021w9rE1sjY5O5dVpumrrz_iUaByGAdzTb1A91XQ')
sheet = ss[0]

# Write to txt file
emailTxt = open('email.txt', 'w') 
for i in range(2, sheet.rowCount + 1):
    cell = sheet['C' + str(i)]
    if cell != None and cell != '':
        emailTxt.write(cell + '\n')
emailTxt.close()