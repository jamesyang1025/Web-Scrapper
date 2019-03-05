from Graph import Graph
import json


def load_data_to_graph(graph):
    """
    Load the data from the json file and create the graph based on it
    """
    with open('data.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

        actors_data = data[0]
        movies_data = data[1]

        for actor in actors_data:
            graph.add_actor(actor, actors_data[actor])

        for movie in movies_data:
            graph.add_movie(movie, movies_data[movie])

        for movie in movies_data:
            actors_list = movies_data[movie]['actors']
            index = 0
            for actor in actors_list:
                length = len(actors_list)
                weight = (length - index) / sum(x for x in range(1, length + 1))
                graph.add_edge(movie, actor, weight)
                index += 1


if __name__ == '__main__':
    graph = Graph()

    load_data_to_graph(graph)

    graph.find_hub_actors()
