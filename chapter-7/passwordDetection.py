import re
def strongPwDetection(password):
    # Has at least 8 character
    atLeast8 = re.compile(r'^.{8,}$')
    mo = atLeast8.search(password)
    if mo == None:
        return 'Password must contains at least 8 character!'
    # Has at least one uppercase character
    hasUppercase = re.compile(r'^.*[A-Z].*$')
    mo = hasUppercase.search(password)
    if mo == None:
        return 'Password must contains at least 1 uppercase character!'
    # Has at least one lowercase character
    hasLowercase = re.compile(r'^.*[a-z].*$')
    mo = hasLowercase.search(password)
    if mo == None:
        return 'Password must contains at least 1 lowercase character!'
    # Has at least one digit character
    hasDigit = re.compile(r'^.*\d.*$')
    mo = hasDigit.search(password)
    if mo == None:
        return 'Password must contains at least 1 digit character!'
    
    return 'Strong password.'

print(strongPwDetection('1234abCD'))