import requests
import re
from bs4 import BeautifulSoup
import logging
import lxml
import json

actors_dict = {}
movies_dict = {}

actors_threshold = 275
movies_threshold = 150


def start_scrapping(start_actor):
    scrape_actor(start_actor)

    i = 0
    j = 0
    while len(actors_dict) < actors_threshold or len(movies_dict) < movies_threshold:
        for index, actor in enumerate(actors_dict):
            if index < i:
                continue

            movies_list = actors_dict[actor]["movies"]
            for movie in movies_list:
                if len(movies_dict) >= movies_threshold:
                    break
                scrape_movie(movie)
            i += 1

        print("movies count = " + str(len(movies_dict)))

        for index, movie in enumerate(movies_dict):
            if index < j:
                continue

            actors_list = movies_dict[movie]["starring"]
            for actor in actors_list:
                if len(actors_dict) >= actors_threshold:
                    break
                scrape_actor(actor)
            j += 1

        print("actors count = " + str(len(actors_dict)))


def scrape_actor(actor_name):
    if actor_name is None:
        logging.error("Actor name is empty")
        return

    url = "https://en.wikipedia.org/wiki/" + actor_name

    page = requests.get(url)
    if page.status_code != 200:
        logging.error("" + url + "cannot be found")
        return

    soup = BeautifulSoup(page.content, 'lxml')
    name = soup.find(id='firstHeading').get_text()
    age = soup.find('span', {'class': 'noprint ForceAgeToShow'})
    if age is None:
        logging.info("Fail to find the age info for " + actor_name)
        return

    age = age.get_text()
    age = int(re.findall('\d+', age)[0])
    movies_table = soup.find('table', {'class': 'wikitable sortable'})
    if movies_table is None:
        logging.info("Fail to find the filmography table for " + actor_name)
        return

    movies = movies_table.find_all('a')
    movies_list = []
    for movie in reversed(movies):
        if movie.get('title') is None:
            logging.info("Not a movie")
            continue

        movies_list.append(movie.get('title'))
    actors_dict[name] = {"name": name, "age": age, "movies": movies_list}


def scrape_movie(movie_name):
    if movie_name is None:
        logging.error("Movie name is empty")
        return

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

    year = ""
    actors = None
    box_office = ""
    for row in info:
        if row.find(string=re.compile("Release date")):
            year = row.get_text()
            year = re.findall(r'\d{4}', year)[0]

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
            box_office = re.findall(r"[-+]?\d*\.\d+|\d+", box_office)[
                0]  # https://stackoverflow.com/questions/4703390/how-to-extract-a-floating-number-from-a-string

            grossing = float(box_office) * 1000000
            grossing = int(grossing)

    if actors is None:
        logging.info("Fail to find starring info for " + movie_name)
        return

    actors_list = []
    for actor in actors:
        if actor.get('title') is None:
            logging.info("Not an actor")
            continue

        actors_list.append(actor.get('title'))

    movies_dict[movie_name] = {"name": name, "grossing": grossing, "year": year, "starring": actors_list}


if __name__ == '__main__':
    start_url = "https://en.wikipedia.org/wiki/Jennifer_Connelly"
    start_actor = "Jennifer Connelly"
    start_scrapping(start_actor)
    # print(actors_dict)
    # print(movies_dict)

    with open("data.json", 'w') as file_out:
        data = {"Actors": actors_dict, "Movies": movies_dict}
        json.dump(data, file_out, indent=4)
        logging.info("Writing to json file completed")
