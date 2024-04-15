# Scrapping
## Parcourir toutes les cqtégories de livre du site
### Vérifier les nombres de livres par catégorie
#### Notifier les catégories ayant un total infeérieur à 30

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
_min = 15


def main():
    with requests.Session() as session:
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # categories_div = soup.find('div', class_='side_categories').find_all('a')
        # Alternative
        categories_div = soup.select("div.side_categories a")

        categories_href = [child.get('href') for child in categories_div]
        categories_name = [child.text.strip() for child in categories_div]

        for idx, category in enumerate(categories_href):
            url_category = f"https://books.toscrape.com/{category}"
            response_category = session.get(url_category)
            soup_category = BeautifulSoup(response_category.text, 'html.parser')
            count_books = soup_category.find('form', class_="form-horizontal").find('strong')
            if int(count_books.text) < _min:
                print(f"La Catégorie {categories_name[idx]} a moins de {_min} livres ({int(count_books.text)})")
            else:
                print("Ok")


if __name__ == "__main__":
    main()
