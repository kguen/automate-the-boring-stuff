import re
def regexStrip(strInput, chr = ' '):
    regex = re.compile(rf"(^[{chr}]*)|([{chr}]*$)")
    return regex.sub('', strInput)

print(regexStrip('yrtxxxxrty', 'ryt'))
print(len(regexStrip('   xxxx   ')))