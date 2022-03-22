import requests
from bs4 import BeautifulSoup
page = r'https://webscraper.io/test-sites/e-commerce/allinone'

page = requests.get(page)
page = page.text
soup = BeautifulSoup(page, 'html.parser')
#page = soup.find_all(class_='caption')
#page = soup.find_all(class_='thumbnail')
page = soup.find_all(class_='row', limit=2)[1]

#page = page.find_all('div')
print(page.get_text())
for i in page:
    page = soup.find_all(class_='col-sm-4 col-lg-4 col-md-4')
    print(page.get_text())
    for l in page:
        page = soup.find_all(class_='thumbnail')
    print(page.get_text())