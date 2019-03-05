import operator
import matplotlib.pyplot as plt


class Actor:

    def __init__(self, name, age, grossing, movies):
        """
        Initialization of the Actor node class
        :param name: the actor's name
        :param age: the actor's age
        :param grossing: the actor's grossing
        :param movies: the list of movies the actor is in
        """
        self.name = name
        self.age = age
        self.grossing = grossing
        self.movies = movies


class Movie:

    def __init__(self, name, grossing, year, starring):
        """
        Initialization of the Movie node class
        :param name: the movie's name
        :param grossing: the movie's grossing
        :param year: the movie's released year
        :param starring: the movie's starring cast
        """
        self.name = name
        self.grossing = grossing
        self.year = year
        self.starring = starring


class Graph:

    def __init__(self):
        """
        Initialization of the Graph class
        """
        self.actors = []
        self.movies = []
        self.edges = []

    def add_actor(self, actor_name, actor_data):
        """
        Add an actor node to the graph
        :param actor_name: the actor's name
        :param actor_data: the actor's data
        """
        actor = Actor(actor_name, actor_data["age"], actor_data["total_gross"], actor_data["movies"])
        self.actors.append(actor)

    def add_movie(self, movie_name, movie_data):
        """
        Add a movie node to the graph
        :param movie_name: the movie's name
        :param movie_data: the movie's data
        """
        movie = Movie(movie_name, movie_data["box_office"], movie_data["year"], movie_data["actors"])
        self.movies.append(movie)

    def add_edge(self, movie_name, actor_name, weight):
        """
        Add an edge to the graph
        :param movie_name: the movie's name
        :param actor_name: the actor's name
        :param weight: the weight of the edge, with actors at the top of the cast having more weight
        """
        movie = None
        for m in self.movies:
            if m.name == movie_name:
                movie = m

        actor = None
        for a in self.actors:
            if a.name == actor_name:
                actor = a

        if actor is None or movie is None:
            return
        edge = (movie, actor, weight)
        self.edges.append(edge)

    def find_hub_actors(self):
        """
        Find the hub actors in the graph and plot the top 20 hub actors
        :return the hub actor
        """
        hub_dict = {}

        for i in range(len(self.actors)):
            actor = self.actors[i].name
            movies_list = self.actors[i].movies
            connections = []
            for movie in movies_list:
                edges_dict = {}
                for e in self.edges:
                    if e[0].name == movie:
                        edges_dict[e[1].name] = e

                if actor in edges_dict:
                    for e in edges_dict.values():
                        if e[1].name != actor and e[1].name not in connections:
                            connections.append(e[1].name)

            hub_dict[actor] = len(connections)

        sorted_hub_dict = sorted(hub_dict.items(), key=operator.itemgetter(1), reverse=True)

        names = [x[0] for x in sorted_hub_dict]
        scores = [x[1] for x in sorted_hub_dict]

        print("The \"hub\" actor is " + names[0])

        plt.bar(names[:20], scores[:20])
        plt.xticks(rotation=90)
        plt.show()

        return names[0]

    def find_most_grossing_age_group(self):
        """
        Find and plot the age groups that generates most amount of money
        :return the age group that generates the most amount of money
        """
        ages_grossing = {}

        for actor in self.actors:
            age = actor.age
            if age not in ages_grossing:
                ages_grossing[actor.age] = actor.grossing
            else:
                ages_grossing[actor.age] += actor.grossing

        age_group_grossing = {}
        i = 1
        j = 5
        while j <= 100:
            age_group_grossing['' + str(i) + '-' + str(j)] = 0
            age_group_grossing['' + str(i) + '-' + str(j)] = sum([v for k, v in ages_grossing.items() if i <= k <= j])
            i += 5
            j += 5

        print("The age group that generates the most amount of money is " +
              max(age_group_grossing.items(), key=operator.itemgetter(1))[0])

        plt.bar(age_group_grossing.keys(), age_group_grossing.values())
        plt.xticks(rotation=90)
        plt.show()

        return max(age_group_grossing.items(), key=operator.itemgetter(1))[0]
