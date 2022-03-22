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

#title List of Available Champions
listtitle = classprincipale.find(class_='mw-headline').get_text()
Content['title']= listtitle
#legende

wikitable = classprincipale.find(class_='wikitable')
wikitable = wikitable.tbody
wikitable = wikitable.find_all('tr')
for row in wikitable:
    column= row.find_all('td')
    
    
    print(column)


#rows = rows.find('tr')

    

print (En_tete,'\n',Content )

#List of Available Champions
List = {}
lac = classprincipale.find(class_='article-table')
rows = lac.find_all('tr')
for row in rows:
    column= row.get_text().strip().replace('\n',' ').split(' ')
    column = [x for x in column if x != '']
    print(column)
    if len(column) == 5:
     column = [column[0]+ ' ' +column[1] ]
    if len(column) == 6:
     column = [column[0]+ ' ' +column[1] + ' ' + column[2] ]
    if len(column) == 7:
     column = [column[0]+ ' ' +column[1] + ' ' + column[2] ]
    elif len(column) == 8:
        column = [column[0]+ ' ' +column[1] + ' ' + column[2] ]
    elif len(column) == 9:
        column = [column[0]+ ' ' +column[1] + ' ' + column[2]+ ' ' + column[3]]
    elif len(column) == 10:
        column = [column[0]+ ' ' +column[1] + ' ' + column[2]+ ' ' + column[3] ]
    elif len(column) == 11:
        column = [column[0]+ ' ' +column[1] + ' ' + column[2]+ ' ' + column[3]+'' +column[4] ]
    elif len(column) == 12:
        column = [column[0]+ ' ' +column[1] + ' ' + column[2]+ ' ' + column[3]+'' +column[4]+ ' ' + column[5] ]
    
    print(column)
        #List['column'] = column
        #print(List)
