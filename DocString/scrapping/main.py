import requests
from bs4 import BeautifulSoup
from pprint import pprint

from utils import traverse_dom

# url = "https://www.docstring.fr/api/books_to_scrape/index.html"
# url_2 = "https://books.toscrape.com"
# response = requests.get(url_2)

# with open('index.html', 'w') as f:
#     f.write(response.text)

with open('index.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
aside = soup.find('div', class_="side_categories")
categories_div = aside.find('ul').find('li').find('ul')
categories = [child.text.strip() for child in categories_div.children if child.name]

images = soup.find('section').find_all('img')
for image in images:
    pass
    # pprint(image.get('src'))

# Ma méthode pour récupérer tous les titres
books_title_h3 = soup.find_all('h3')
books_title = [child.find('a').get('title') for child in books_title_h3]
for book_title in books_title:
    pass
    # pprint(book_title)

# La méthode de DocString - En Spécifiant les
titles_tag = [title.get('title') for title in soup.find_all('a', title=True)]
pprint(titles_tag)
# Commencer le parcours depuis la racine de l'arbre DOM
# traverse_dom(soup)
