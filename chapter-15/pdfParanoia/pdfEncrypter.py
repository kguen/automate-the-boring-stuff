from pathlib import Path
import os, sys, PyPDF2

# Get encrypt password from cmd args
password = sys.argv[1]

for folderName, _, fileNames in os.walk(Path.cwd()):
    for fileName in fileNames:
        # Get full file path
        filePath = Path(folderName) / fileName
        if filePath.suffix == '.pdf':
            print(f'Encrypting {filePath}...')
            originalPdf = open(filePath, 'rb')
            
            # Create reader and writer
            pdfReader = PyPDF2.PdfFileReader(originalPdf)
            if pdfReader.isEncrypted: # Skip encrypted files
                continue
            pdfWriter = PyPDF2.PdfFileWriter()
            
            # Read and add all pages from original pdf to pdfWriter
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            
            # Encrypt with password
            pdfWriter.encrypt(password)
            
            # Write encryted pdf to a new pdf file
            newFilePath = Path(folderName) / f'{filePath.stem}_encrypted.pdf'
            resultPdf = open(newFilePath, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            
            # Testing before delete original file
            pdfReader = PyPDF2.PdfFileReader(open(newFilePath, 'rb'))
            if pdfReader.decrypt(password) != 0:
                # Delete original file
                originalPdf.close()
                os.unlink(str(filePath))
                print(f'Encrypted to {newFilePath}.')