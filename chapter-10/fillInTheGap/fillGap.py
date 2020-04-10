from pathlib import Path
import re, shutil

folderPath = Path.cwd() / 'chapter-10/fillInTheGap'

def fillGap(prefix):
    # Get and sort all files match with prefix
    globPattern = f'{prefix}???.*'
    matchFiles = sorted(list(folderPath.glob(globPattern)))
    # create regex to get indexed part in file name
    regex = re.compile(re.escape(prefix) + r'(\d{3})')

    prevIdx = None
    for filePath in matchFiles:
        mo = regex.search(filePath.stem)
        if mo is None:
            continue
        currentIdx = int(mo.group(1))
        # first index
        if prevIdx is None:
            prevIdx = currentIdx
            continue
        # gaps between current index and previous index
        if currentIdx - prevIdx > 1:
            # change index and add leading zeros
            currentIdx = str(prevIdx + 1).zfill(3)
            shutil.move(filePath, folderPath / f'{prefix}{currentIdx}{filePath.suffix}')
        prevIdx += 1

def createGap(prefix, index):
    # Get and sort all files match with prefix
    globPattern = f'{prefix}???.*'
    matchFiles = sorted(list(folderPath.glob(globPattern)), reverse=True)
    # create regex to get indexed part in file name
    regex = re.compile(re.escape(prefix) + r'(\d{3})')

    for filePath in matchFiles:
        mo = regex.search(filePath.stem)
        if mo is None:
            continue
        currentIdx = int(mo.group(1))
        # gaps between current index and previous index
        if currentIdx >= index:
            # change index and add leading zeros
            currentIdx = str(currentIdx + 1).zfill(3)
            shutil.move(filePath, folderPath / f'{prefix}{currentIdx}{filePath.suffix}')
        else: break

fillGap('spam')
# createGap('spam', 3)