import os
import unittest

from API import app


class TestAPI(unittest.TestCase):

    def test_filter_actor(self):
        with app.test_client() as client:
            result = client.get('/actors?name=\"Jessica\"&age=28')

            json = [
                {
                    "age": 28,
                    "json_class": "Actor",
                    "movies": [
                        "Autopsy",
                        "The Haunting of Molly Hartley",
                        "Altitude",
                        "The Devil's Carnival",
                        "Eden",
                        "The Prince",
                        "Larry Gaye: Renegade Male Flight Attendant",
                        "Abattoir"
                    ],
                    "name": "Jessica Lowndes",
                    "total_gross": 0
                }
            ]
            self.assertEqual(result.get_json(), json)

    def test_filter_movie(self):
        with app.test_client() as client:
            result = client.get('/movies?name=\"City\"&year=1992')

            json = [
                {
                    "actors": [
                        "Robert De Niro",
                        "Jessica Lange",
                        "Cliff Gorman",
                        "Jack Warden",
                        "Alan King"
                    ],
                    "box_office": 6202756,
                    "json_class": "Movie",
                    "name": "Night and the City",
                    "wiki_page": "https://en.wikipedia.org/wiki/Night_and_the_City_(1992_film)",
                    "year": 1992
                }
            ]
            self.assertEqual(result.get_json(), json)

    def test_get_actor(self):
        with app.test_client() as client:
            result = client.get('/actors/Jane March')

            json = {
                "age": 43,
                "json_class": "Actor",
                "movies": [
                    "The Lover",
                    "Color of Night",
                    "Never Ever",
                    "Tarzan and the Lost City",
                    "Provocateur",
                    "Beauty and the Beast",
                    "The Stone Merchant",
                    "My Last Five Girlfriends",
                    "Clash of the Titans",
                    "Stalker",
                    "Will",
                    "Grimm's Snow White",
                    "Jack the Giant Killer"
                ],
                "name": "Jane March",
                "total_gross": 19750470
            }

            self.assertEqual(result.get_json(), json)

    def test_get_movie(self):
        with app.test_client() as client:
            result = client.get('/movies/Sin City')

            json = {
                "actors": [
                    "Bruce Willis",
                    "Mickey Rourke",
                    "Clive Owen",
                    "Jessica Alba",
                    "Benicio del Toro",
                    "Brittany Murphy",
                    "Elijah Wood"
                ],
                "box_office": 158,
                "json_class": "Movie",
                "name": "Sin City",
                "wiki_page": "https://en.wikipedia.org/wiki/Sin_City_(film)",
                "year": 0
            }

            self.assertEqual(result.get_json(), json)

    def test_update_actor(self):
        with app.test_client() as client:
            result = client.put('/actors/Jessica Alba', json={"age": 18})

            json = {
                "age": 18,
                "json_class": "Actor",
                "movies": [
                    "Camp Nowhere",
                    "Venus Rising",
                    "P.U.N.K.S.",
                    "Never Been Kissed",
                    "Idle Hands",
                    "Paranoid",
                    "The Sleeping Dictionary",
                    "Honey",
                    "Sin City",
                    "Fantastic Four",
                    "Into the Blue",
                    "Knocked Up",
                    "Fantastic Four: Rise of the Silver Surfer",
                    "The Ten",
                    "Good Luck Chuck",
                    "Awake",
                    "The Eye",
                    "Meet Bill",
                    "The Love Guru",
                    "Valentine's Day",
                    "The Killer Inside Me",
                    "Machete",
                    "An Invisible Sign",
                    "Little Fockers",
                    "Spy Kids 4: All the Time in the World",
                    "A.C.O.D.",
                    "Escape from Planet Earth",
                    "Machete Kills",
                    "Sin City: A Dame to Kill For",
                    "Dear Eleanor",
                    "Some Kind of Beautiful",
                    "Stretch",
                    "Barely Lethal",
                    "Entourage",
                    "The Veil",
                    "Mechanic: Resurrection"
                ],
                "name": "Jessica Alba",
                "total_gross": 197
            }

            self.assertEqual(result.get_json(), json)

    def test_update_movie(self):
        with app.test_client() as client:
            result = client.put('/movies/Sin city', json={"year": 2005})

            json = {
                "actors": [
                    "Bruce Willis",
                    "Mickey Rourke",
                    "Clive Owen",
                    "Jessica Alba",
                    "Benicio del Toro",
                    "Brittany Murphy",
                    "Elijah Wood"
                ],
                "box_office": 158,
                "json_class": "Movie",
                "name": "Sin City",
                "wiki_page": "https://en.wikipedia.org/wiki/Sin_City_(film)",
                "year": 2005
            }

            self.assertEqual(result.get_json(), json)

    def test_add_actor(self):
        with app.test_client() as client:
            result = client.post('/actors/add_actor', json={
                "age": 20,
                "json_class": "Actor",
                "movies": [
                    "A",
                    "B",
                    "C"
                ],
                "name": "Billy Joe",
                "total_gross": 123456
            })

            json = {
                "age": 20,
                "json_class": "Actor",
                "movies": [
                    "A",
                    "B",
                    "C"
                ],
                "name": "Billy Joe",
                "total_gross": 123456
            }

            self.assertEqual(result.get_json(), json)

    def test_add_movie(self):
        with app.test_client() as client:
            result = client.post('/movies/add_movie', json={
                "actors": [
                    "Bruce Willis",
                    "Mickey Rourke",
                    "Clive Owen",
                    "Jessica Alba"
                ],
                "box_office": 233,
                "json_class": "Movie",
                "name": "Divine City",
                "wiki_page": "https://en.wikipedia.org/wiki/Divine_City)",
                "year": 2025
            })

            json = {
                "actors": [
                    "Bruce Willis",
                    "Mickey Rourke",
                    "Clive Owen",
                    "Jessica Alba"
                ],
                "box_office": 233,
                "json_class": "Movie",
                "name": "Divine City",
                "wiki_page": "https://en.wikipedia.org/wiki/Divine_City)",
                "year": 2025
            }

            self.assertEqual(result.get_json(), json)

    def test_delete_actor(self):
        with app.test_client() as client:
            result = client.get('/actors/James Whitmore')

            json = {
                "age": 87,
                "json_class": "Actor",
                "movies": [
                    "Command Decision",
                    "Battleground",
                    "Give 'em Hell, Harry!",
                    "Glory! Glory!",
                    "The Practice",
                    "Here's to Life!",
                    "Mister Sterling"
                ],
                "name": "James Whitmore",
                "total_gross": 6269000
            }

            self.assertEqual(result.get_json(), json)

            result_2 = client.delete('/actors/James Whitmore')

            json_2 = {
                "Success": "Deletion completed"
            }
            self.assertEqual(result_2.get_json(), json_2)

            result_3 = client.get('/actors/James Whitmore')

            json_3 = {
                "error": "Not found"
            }
            self.assertEqual(result_3.get_json(), json_3)

    def test_delete_movie(self):
        with app.test_client() as client:
            result = client.get('/movies/Blaze')

            json = {
                "actors": [
                    "Paul Newman",
                    "Lolita Davidovich"
                ],
                "box_office": 19131246,
                "json_class": "Movie",
                "name": "Blaze",
                "wiki_page": "https://en.wikipedia.org/wiki/Blaze_(film)",
                "year": 1989
            }

            self.assertEqual(result.get_json(), json)

            result_2 = client.delete('/movies/Blaze')

            json_2 = {
                "Success": "Deletion completed"
            }
            self.assertEqual(result_2.get_json(), json_2)

            result_3 = client.get('/movies/Blaze')

            json_3 = {
                "error": "Not found"
            }
            self.assertEqual(result_3.get_json(), json_3)


if __name__ == '__main__':
    app.testing = True

    unittest.main()
