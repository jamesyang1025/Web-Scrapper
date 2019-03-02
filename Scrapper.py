import requests
import re
from bs4 import BeautifulSoup
import logging
import lxml

actors_dict = {}
movies_dict = {}

def start_page(url):
    page = requests.get(url)

    if page.status_code != 200:
        logging.error('Cannot open the url link')
        return

    soup = BeautifulSoup(page.content, 'lxml')
    name = soup.find(id='firstHeading').get_text()
    age = soup.find('span', {'class': 'noprint ForceAgeToShow'}).get_text()
    age = int(re.findall('\d+', age)[0])
    movies_table = soup.find('table', {'class': 'wikitable sortable'})
    movies = movies_table.find_all('a')
    movies_list = []
    for movie in reversed(movies):
        movies_list.append(movie.get('title').split('(')[0])
    actors_dict[name] = movies_list

    print("name: " + name)
    print("age: " + str(age))
    print(movies_list)

    return


if __name__ == '__main__':
    start_url = "https://en.wikipedia.org/wiki/Jennifer_Connelly"
    start_page(start_url)
    print(actors_dict)