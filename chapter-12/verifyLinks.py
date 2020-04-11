import requests, sys, bs4

# download website
url = f'https://{sys.argv[1]}'
print(f'Open {url}...')
res = requests.get(f'{url}')
res.raise_for_status()

# get all links from website
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('a')

# try to download every links
print('Finding broken links...')
for elem in linkElems:
    href = elem.get('href')
    if href.startswith('https://'):
        res = requests.get(href)
    else:
        res = requests.get(url + href)
    if res.status_code >= 400:
        print(f'Found broken link: {href}')

print('Done.')