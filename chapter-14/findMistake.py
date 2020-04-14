import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

rowCount = 15000
# Data start from row 2
for row in range(2, rowCount):
    rowValues = ss[0].getRow(row)
    # beansPerJar * jars != totalBeans
    if int(rowValues[0]) * int(rowValues[1]) != int(rowValues[2]):
        # Printing
        print('Found incorrect row: ' + str(row))
        print('-- Beans per jar: ' + rowValues[0])
        print('-- Jars: ' + rowValues[1])
        print('-- Expected: %s' % (int(rowValues[0]) * int(rowValues[1])))
        print('-- Actual: ' + rowValues[2])