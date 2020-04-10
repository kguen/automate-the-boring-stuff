import os
from pathlib import Path

for folderName, _, fileNames in os.walk(Path.cwd()):
    for fileName in fileNames:
        filePath = Path(folderName) / fileName
        if os.path.getsize(filePath) > 5000: # larger than 5000 bytes
            print(filePath)