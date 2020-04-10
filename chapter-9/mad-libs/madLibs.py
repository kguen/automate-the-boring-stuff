import re
from pathlib import Path

# Regex to find all occurences in order
regex = re.compile('ADJECTIVE|NOUN|VERB')

# Read content from template
templateFile = open('chapter-9/mad-libs/template.txt')
template = templateFile.read()

# Find and replace all occurences
occurences = regex.findall(template)
for item in occurences:
    strInput = input(f'Enter an {item.lower()}:\n')
    template = template.replace(item, strInput, 1)

print(template)

# Write result into a new file
resultFile = open('chapter-9/mad-libs/result.txt', 'w')
resultFile.write(template)
resultFile.close()