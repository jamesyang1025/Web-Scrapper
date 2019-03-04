import json
from Graph import Graph


def load_data_to_graph(graph):
    """
    Load the data from the json file and create the graph based on it
    """
    with open('data.json') as json_file:
        data = json.load(json_file)

        actors_data = data['Actors']
        for actor in actors_data:
            graph.add_actor(actor, actors_data[actor])

        movies_data = data['Movies']
        for movie in movies_data:
            graph.add_movies(movie, movies_data[movie])

        for movie in movies_data:
            starring_list = movies_data[movie]['starring']
            index = 0
            for actor in starring_list:
                length = len(starring_list)
                weight = (length - index) / sum(x for x in range(1, length + 1))
                graph.add_edge(movie, actor, weight)
                index += 1


if __name__ == '__main__':
    graph = Graph()

    load_data_to_graph(graph)

    print("Database set up complete. Please select how you want to interact with it. :)")

    # Graph queries part
    while True:
        action = input("\n"
                       "[1] Find how much a movie has grossed\n"
                       "[2] List which movies an actor has worked in\n"
                       "[3] List which actors worked in a movie\n"
                       "[4] List the top X actors with the most total grossing value\n"
                       "[5] List the oldest X actors\n"
                       "[6] List all the movies for a given year\n"
                       "[7] List all the actors for a given year\n")
        if action not in "1234567" or len(action) != 1:
            print("Invalid input. Please input again. :)\n")
            continue
        if action == '1':
            print("You selected: [1] Find how much a movie has grossed\n")

            movie = input("Please enter the movie's name\n")

            graph.print_movie_grossing(movie)

        elif action == '2':
            print("You selected: [2] List which movies an actor has worked in\n")

            actor = input("Please enter the actor's name\n")

            graph.print_movies_for_actor(actor)

        elif action == '3':
            print("You selected: [3] List which actors worked in a movie\n")

            movie = input("Please enter the movie's name\n")

            graph.print_actors_for_movie(movie)

        elif action == '4':
            print("You selected: [4] List the top X actors with the most total grossing value\n")

            x = int(input("Please enter the top X number\n"))

            graph.print_top_x_grossing_actors(x)

        elif action == '5':
            print("You selected: [5] List the oldest X actors\n")

            x = int(input("Please enter the oldest X number\n"))

            graph.print_oldest_x_actor(x)

        elif action == '6':
            print("You selected: [6] List all the movies for a given year\n")

            year = input("Please enter the year\n")

            graph.print_movies_in_given_year(year)

        elif action == '7':
            print("You selected: [7] List all the actors for a given year\n")

            year = input("Please enter the year\n")

            graph.print_actors_in_given_year(year)
