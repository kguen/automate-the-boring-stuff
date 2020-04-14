import sys, ezsheets
# Get file name and convert format from cmd args
fileName = sys.argv[1]
format = sys.argv[2]

# Upload file to google sheets
ss = ezsheets.upload(fileName + '.xlsx')

# Call download function using string name
getattr(ss, 'downloadAs' + format.upper())()