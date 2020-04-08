import re
def dateDetection(date):
    dateRegex = re.compile(r'^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/([12][0-9][0-9][0-9])$')
    mo = dateRegex.search(date)
    if mo == None:
        return False
    
    # Number of days in each month
    daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    # Input date parsed into day, month and year
    day = int(mo.group(1))
    month = int(mo.group(2))
    year = int(mo.group(3))

    # If input date is in leap year => increase number of days in Feb to 29
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        daysOfMonth[1] += 1
    # month - 1 match with daysOfMonth index
    if day > daysOfMonth[month - 1]:
        return False
    return True

print(dateDetection('29/02/2000'))