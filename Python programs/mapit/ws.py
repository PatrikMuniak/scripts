
#! python3
import requests, sys, webbrowser, bs4
print('Googling...')
res=requests.get('http://www.google.com/search?q='+'+'.join(sys.argv[1:]))
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)

linkElms=soup.select('.r a')

numOpen=min(5, len(linkElms))
for i in range(numOpen):
    webbrowser.open('http://google.com/'+linkElms[i].get('href'))
