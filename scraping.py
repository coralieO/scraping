import requests
from bs4 import BeautifulSoup
page = r'https://www.imdb.com/chart/top'

page = requests.get(page)
page = page.text
soup = BeautifulSoup(page, 'html.parser')
print(x.get_text() for x in soup.find_all(class_='titleColumn'))
# print(soup.find_all(class_='ratingColumn'))