
import requests
import webbrowser
import bs4, pprint
keywords=['road','bike'] #Provvisory: change with sys.argv()
ebayserp= requests.get('https://www.ebay.co.uk/sch/i.html?_nkw='+'+'.join(keywords), 'rb')

bs=bs4.BeautifulSoup(ebayserp.text, 'html.parser')
print(str(len(ebayserp.text)))

#gathering titles of ads
adnamesraw=[]
for name in bs.find_all('a'):
    adnamesraw.append(name.string)
adnames=[]   
for i in adnamesraw:
    if adnamesraw!= '' or None:
        adnames.append(i)


print(adnames[0:40])
savetxt=open('savehere.txt', 'w')
savetxt.write(bin(adnames))

