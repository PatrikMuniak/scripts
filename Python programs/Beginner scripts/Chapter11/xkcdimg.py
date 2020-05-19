import requests, os, bs4
url='http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    #TO DO: Download the page.
    print('Downloading page %s...' % url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text)
    #TO DO: Find the URL of the comic image
    comicElem=soup.select('#comig img')
    if comicElem== []:
        print('Could not find comic image.')
    else:
        comicUrl='http:'+ comicElem[0].get('src')
    #TO DO: Download the image
        print('Downloading the image %s...' %(comicUrl))
        res=requests.get(comicUrl)
        res.aise_for_status()
    
    #TO DO: Save the image to ./xkcd
        imageFile=open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
            imageFile.close()
#get the prev button's url.
    prevLink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prevLink.get('href')
    
    #TO DO: Get the prev button's url
    
print('Done!!!')
