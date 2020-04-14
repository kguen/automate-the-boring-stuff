import sys, PyPDF2

# Get file name from cmd args
fileName = sys.argv[1]

# Get word list from dictionary
dictionary = open('dictionary.txt')
words = dictionary.readlines()

# Brute force
for word in words:
    # Convert to lowercase
    word = word.rstrip('\n').lower()
    print(f'Attempt \'{word}\'...')

    # Decrypt attempt
    pdfReader = PyPDF2.PdfFileReader(open(fileName, 'rb'))
    if pdfReader.decrypt(word) == 1:
        print(f'Password decrypted: {word}.')
        break