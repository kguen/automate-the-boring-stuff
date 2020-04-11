import requests, sys, bs4, os

searchTerm = ' '.join(sys.argv[1:]) # get search term from cmd
os.makedirs(f'flickr/{searchTerm}', exist_ok=True) # store images in ./flickr

# open flickr
print('Searching...')
res = requests.get(f'https://flickr.com/search?text={searchTerm}')
res.raise_for_status()

# make soup and find all images (thumbnails only)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
imageElems = soup.select('.view.photo-list-photo-view')

# download images
if imageElems == []:
    print('Could not find images.')
else:
    for elem in imageElems:
        styles = elem.get('style').split(';') # split element style into values 
        for style in styles:
            kvPair = style.split(':') # split each style into a key-value pair
            if kvPair[0].strip() == 'background-image':
                # value = url(...) => image link is the substring start from '(' to ')'
                imageUrl = kvPair[1][kvPair[1].find('(')+1:kvPair[1].find(')')]
                # download image
                print(f'Downloading image {imageUrl}...')
                res = requests.get(f'https:{imageUrl}')
                res.raise_for_status()
                # save image to folder
                imageFile = open(os.path.join(f'flickr/{searchTerm}', os.path.basename(imageUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
print('Done.')