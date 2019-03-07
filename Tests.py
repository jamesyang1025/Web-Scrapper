import unittest
from Graph import Graph
import Main


class TestGraph(unittest.TestCase):

    def test_print_movie_grossing(self):
        graph = Graph()

        Main.load_data_to_graph(graph)

        self.assertEqual(20500000, graph.print_movie_grossing("Top Secret!"))

    def test_print_movies_for_actor(self):
        graph = Graph()

        Main.load_data_to_graph(graph)

        list = [
                "Alita: Battle Angel",
                "Prowler (comics)",
                "Spider-Man: Into the Spider-Verse",
                "Don Shirley",
                "Green Book (film)",
                "Roxanne Roxanne",
                "Hidden Figures",
                "Moonlight (2016 film)",
                "Free State of Jones (film)",
                "Kicks (film)",
                "The Hunger Games: Mockingjay \u2013 Part 2",
                "List of The Hunger Games characters",
                "The Hunger Games: Mockingjay \u2013 Part 1",
                "Supremacy (film)",
                "Go for Sisters",
                "The Place Beyond the Pines",
                "Predators (film)",
                "Crossing Over (film)",
                "The Curious Case of Benjamin Button (film)",
                "Making Revolution"
            ]

        self.assertEqual(list, graph.print_movies_for_actor("Mahershala Ali"))

    def test_print_actors_for_movie(self):
        graph = Graph()

        Main.load_data_to_graph(graph)

        list = [
                "Tom Holland (actor)",
                "Michael Keaton",
                "Jon Favreau",
                "Zendaya",
                "Donald Glover",
                "Tyne Daly",
                "Marisa Tomei",
                "Robert Downey Jr."
            ]

        self.assertEqual(list, graph.print_actors_for_movie("Spider-Man: Homecoming"))

    def test_print_top_x_grossing_actors(self):
        graph = Graph()

        Main.load_data_to_graph(graph)

        list = ['Jennifer Connelly', 'Val Kilmer', 'Miles Teller']

        self.assertEqual(list, graph.print_top_x_grossing_actors(3))

    def test_print_oldest_x_actor(self):
        graph = Graph()

        Main.load_data_to_graph(graph)

        list = ['Eva Marie Saint',
                'Hal Holbrook',
                'Rip Torn',
                'Ellen Burstyn',
                'Alan Arkin']

        self.assertEqual(list, graph.print_oldest_x_actor(5))

    def test_print_movies_in_given_year(self):
        graph = Graph()

        Main.load_data_to_graph(graph)

        list = ['Alita: Battle Angel',
                'The New Mutants (film)',
                'The Report (2019 film)']

        self.assertEqual(list, graph.print_movies_in_given_year("2019"))

    def test_print_actors_in_given_year(self):
        graph = Graph()

        Main.load_data_to_graph(graph)

        list = ['Miles Teller',
                'Val Kilmer',
                'Jennifer Connelly',
                'Glen Powell',
                'Jon Hamm',
                'Ed Harris']

        self.assertEqual(list, graph.print_actors_in_given_year("2020"))


if __name__ == '__main__':
    unittest.main()
