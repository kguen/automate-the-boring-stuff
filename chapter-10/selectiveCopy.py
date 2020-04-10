import shutil, os 
from pathlib import Path

def selectiveCopy(suffix):
    for folderName, _, fileNames in os.walk(Path.cwd()):
        folderPath = Path(folderName)
        # skip backup folder
        if folderPath.name == 'selectiveCopy_backup':
            continue
        for fileName in fileNames:
            # get full file path
            filePath = folderPath / fileName
            if filePath.suffix == suffix: 
                shutil.copy(filePath, Path.cwd() / 'selectiveCopy_backup')

selectiveCopy('.doc')
selectiveCopy('.docx')