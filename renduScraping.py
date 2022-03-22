import requests
from bs4 import BeautifulSoup

page = r'https://leagueoflegends.fandom.com/wiki/List_of_champions'
page = requests.get(page)
page = page.text
soup =  BeautifulSoup(page, 'html.parser')
page = soup.main

##Title
leagetitle = page.find(class_='page-header__bottom')
leagetitle = leagetitle.find('h1').get_text().replace('\n',' ').strip()
En_tete = {}
En_tete["title"]= leagetitle

##see also
leagesee = page.find(class_='dablink').get_text().replace('\n',' ')
En_tete['See also']= leagesee

##description
classprincipale = page.find(class_='mw-parser-output')
leagedesc = classprincipale.p.get_text().replace('.\n','')
En_tete['description']= leagedesc

#content
Content = {}
toc = page.find(class_='toc')
toctitle = toc.find(class_='toctitle')
leagecontentTitle = toctitle.h2.get_text()
Content['ContentTitle']= leagecontentTitle

#contentlist
contentlist = toc.ul.get_text().replace('\n',' ')
Content['contentlist']= contentlist

#List of Available Champions
listtitle = classprincipale.find(class_='mw-headline').get_text()
Content['title']
print(listtitle)
print (En_tete,Content )

