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

        edge = (movie, actor, weight)
        self.edges.append(edge)

    def print_movie_grossing(self, movie_name):
        """
        Print the grossing information for the input movie
        :param movie_name: the input movie
        :return the grossing of the movie
        """

        for movie in self.movies:
            if movie.name == movie_name:
                print("$" + str(movie.grossing))
                return movie.grossing

    def print_movies_for_actor(self, actor_name):
        """
        Print all the movies the actor has worked in
        :param actor_name: the actor's name
        :return the movie name
        """
        for actor in self.actors:
            if actor.name == actor_name:
                for movie in actor.movies:
                    print(movie)
                return actor.movies

    def print_actors_for_movie(self, movie_name):
        """
        Print all the actors that worked in the movie
        :param movie_name: the movie's name
        :return the starring list of the movie
        """
        for movie in self.movies:
            if movie.name == movie_name:
                for actor in movie.starring:
                    print(actor)
                return movie.starring

    def print_top_x_grossing_actors(self, x):
        """
        Print the top X actors with the most total grossing value
        :param x: the top X actors
        :return the list of the top X grossing actors
        """
        sorted_list = sorted(self.actors, key=lambda actor: actor.grossing, reverse=True)
        ret_list = []
        for i in range(x):
            print(sorted_list[i].name)
            ret_list.append(sorted_list[i].name)
        return ret_list

    def print_oldest_x_actor(self, x):
        """
        Print the oldest X actor
        :param x: the top X actors
        :return the list of the oldest X actors
        """
        sorted_list = sorted(self.actors, key=lambda actor: actor.age, reverse=True)
        ret_list = []
        for i in range(x):
            print(sorted_list[i].name)
            ret_list.append(sorted_list[i].name)
        return ret_list

    def print_movies_in_given_year(self, year):
        """
        Print all the movies in a given year
        :param year: the input year
        :return the list of movies in the given year
        """
        list = [movie for movie in self.movies if movie.year == year]

        ret_list = []
        for m in list:
            print(m.name)
            ret_list.append(m.name)
        return ret_list

    def print_actors_in_given_year(self, year):
        """
        Print all the actors in a given year
        :param year: the input year
        :return the list of actors in the given year
        """
        movies_list = [movie for movie in self.movies if movie.year == year]

        ret_list = []
        for m in movies_list:
            for actor in m.starring:
                print(actor)
                ret_list.append(actor)
        return ret_list
