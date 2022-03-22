import requests
from bs4 import BeautifulSoup

page = r'https://www.scrapethissite.com/pages/forms/'
page = requests.get(page)
page = page.text
soup =  BeautifulSoup(page, 'html.parser')

page = soup.find('table')
rows = page.find_all('tr')
for row in rows:
    column= row.get_text().strip().replace('\n',' ').split(' ')
    column = [x for x in column if x != '']
    print(column)




