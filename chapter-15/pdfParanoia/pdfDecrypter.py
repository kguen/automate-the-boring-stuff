from pathlib import Path
import os, sys, PyPDF2

# Get decrypt password from cmd args
password = sys.argv[1]

for folderName, _, fileNames in os.walk(Path.cwd()):
    for fileName in fileNames:
        # Get full file path
        filePath = Path(folderName) / fileName
        if filePath.suffix == '.pdf':
            print(f'Decrypting {filePath}...')
            originalPdf = open(filePath, 'rb')

            # Create reader and writer
            pdfReader = PyPDF2.PdfFileReader(originalPdf)
            if not pdfReader.isEncrypted: # Skip decrypted files
                continue
            pdfWriter = PyPDF2.PdfFileWriter()

            # Decrypt and copy file content
            pdfReader.decrypt(password)
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))

            # Write decrypted content to a new file
            newFilePath = Path(folderName) / f'{filePath.stem}_decrypted.pdf'
            resultPdf = open(newFilePath, 'wb')
            pdfWriter.write(resultPdf)
            
            # Close files
            resultPdf.close()
            originalPdf.close()