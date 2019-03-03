import requests
import re
from bs4 import BeautifulSoup
import logging
import lxml
import json

actors_dict = {}
movies_dict = {}


def start_scrapping(start_actor):
    scrape_actor(start_actor)

    movies_list = actors_dict[start_actor]['movies']

    for i in range(len(movies_list)):
        scrape_movie(movies_list[i])






def scrape_actor(actor_name):
    url = "https://en.wikipedia.org/wiki/" + actor_name

    page = requests.get(url)
    if page.status_code != 200:
        logging.error("" + url + "cannot be found")
        return

    soup = BeautifulSoup(page.content, 'lxml')
    name = soup.find(id='firstHeading').get_text()
    age = soup.find('span', {'class': 'noprint ForceAgeToShow'}).get_text()
    age = int(re.findall('\d+', age)[0])
    movies_table = soup.find('table', {'class': 'wikitable sortable'})
    movies = movies_table.find_all('a')
    movies_list = []
    for movie in reversed(movies):
        movies_list.append(movie.get('title'))
    actors_dict[name] = {"name": name, "age": age, "movies": movies_list}


def scrape_movie(movie_name):
    url = "https://en.wikipedia.org/wiki/" + movie_name

    page = requests.get(url)
    if page.status_code != 200:
        logging.error("" + url + "cannot be found")
        return

    soup = BeautifulSoup(page.content, 'lxml')
    name = soup.find(id='firstHeading').get_text()
    info_table = soup.find('table', {'class': 'infobox vevent'})
    if info_table is None:
        logging.info("Cannot find info table for " + movie_name)
        return
    info = info_table.find_all('tr')

    actors = None
    box_office = ""
    for row in info:
        if row.find(string=re.compile("Box office")):
            box_office = row.find('td').get_text().split('[')[0]

        if row.find(string=re.compile("Starring")):
            actors = row.find_all('a')

    grossing = 0
    if box_office == "":
        logging.info("Cannot find box office for " + movie_name)
        grossing = 0
    else:
        if "million" in box_office:
            tmp = box_office.split('$')[1]

            box_office = re.findall(r"[-+]?\d*\.\d+|\d+", box_office)[0]

            grossing = float(box_office) * 1000000
            grossing = int(grossing)

    actors_list = []
    for actor in actors:
        actors_list.append(actor.get('title'))

    movies_dict[movie_name] = {"name": name, "grossing": grossing, "starring": actors_list}


if __name__ == '__main__':
    start_url = "https://en.wikipedia.org/wiki/Jennifer_Connelly"
    start_actor = "Jennifer Connelly"
    start_scrapping(start_actor)
    print(actors_dict)
    print(movies_dict)

    with open("data.json", 'w') as file_out:
        data = {"Actors": actors_dict, "Movies": movies_dict}
        json.dump(data, file_out, indent=4)
        logging.info("Writing to json file completed")
