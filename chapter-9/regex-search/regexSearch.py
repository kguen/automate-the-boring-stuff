import re
from pathlib import Path

def regexSearch(regexStr):
    fPath = Path.cwd() / 'chapter-9' / 'regex-search'
    regex = re.compile(regexStr)

    # For all txt files in folder
    for txtPath in fPath.glob('*.txt'):
        # Open txt file
        txtFile = open(txtPath)
        # For all lines in file
        for line in txtFile.readlines():
            if regex.search(line) != None: 
                print(line)

regexSearch(r'lorem')