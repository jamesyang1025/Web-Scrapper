from flask import Flask, jsonify, abort, make_response, request
import json

app = Flask(__name__)


@app.route('/actors', methods=['GET'])
def filter_actor():
    """
    Filter out the actors data that matches the condition
    :return: the filtered actors list
    """
    name = request.args.get('name', default="", type=str)
    age = request.args.get('age', default=-1, type=int)

    filtered_list = []

    if name != "":
        name = name.replace('_', ' ')
        name = name.replace('"', '')
        for actor in actors_data:
            if name.lower() in actor.lower():
                filtered_list.append(actors_data[actor])

    if age != -1:
        filtered_list = [movie for movie in filtered_list if age == movie['age']]

    return make_response(jsonify(filtered_list), 200)


@app.route('/movies', methods=['GET'])
def filter_movie():
    """
    Filter out the movies data that matches the condition
    :return: the filtered movies list
    """
    name = request.args.get('name', default="", type=str)
    year = request.args.get('year', default=-1, type=int)

    filtered_list = []

    if name != "":
        name = name.replace('_', ' ')
        name = name.replace('"', '')
        for movie in movies_data:
            if name.lower() in movie.lower():
                filtered_list.append(movies_data[movie])

    if year != -1:
        filtered_list = [movie for movie in filtered_list if year == movie['year']]

    return make_response(jsonify(filtered_list), 200)


@app.route('/actors/<string:actor_name>', methods=['GET'])
def get_actor(actor_name):
    """
    Return the actor object with the input actor name
    :param actor_name: the actor's name
    :return: the corresponding actor object
    """
    actor_name = actor_name.replace('_', ' ')
    for actor in actors_data:
        if actor.lower() == actor_name.lower():
            return make_response(jsonify(actors_data[actor]), 200)

    abort(404)


@app.route('/movies/<string:movie_name>', methods=['GET'])
def get_movie(movie_name):
    """
    Return the actor object with the input actor name
    :param movie_name: the actor's name
    :return: the corresponding actor object
    """
    movie_name = movie_name.replace('_', ' ')
    for movie in movies_data:
        if movie.lower() == movie_name.lower():
            return make_response(jsonify(movies_data[movie]), 200)

    abort(404)


@app.route('/actors/<string:actor_name>', methods=['PUT'])
def update_actor(actor_name):
    """
    Update the input actor's data
    :param actor_name: the actor to update
    :return: the updated actor object
    """
    actor_name = actor_name.replace('_', ' ')
    for actor in actors_data:
        if actor.lower() == actor_name.lower():
            if not request.json:
                abort(400)

            for key in request.json:
                actors_data[actor][key] = request.json[key]

            return make_response(jsonify(actors_data[actor]), 200)

    abort(404)


@app.route('/movies/<string:movie_name>', methods=['PUT'])
def update_movie(movie_name):
    """
    Update the input movie data
    :param movie_name: the movie to update
    :return: the updated movie object
    """
    movie_name = movie_name.replace('_', ' ')
    for movie in movies_data:
        if movie.lower() == movie_name.lower():
            if not request.json:
                abort(400)

            for key in request.json:
                movies_data[movie][key] = request.json[key]

            return make_response(jsonify(movies_data[movie]), 200)

    abort(404)


@app.route('/actors/add_actor', methods=['POST'])
def add_actor():
    """
    Add an actor to the data
    :return: the new actor object
    """
    if not request.json or 'json_class' not in request.json or 'name' not in request.json or 'age' not in request.json \
            or 'total_gross' not in request.json or 'movies' not in request.json:
        abort(400)

    name = request.json['name']

    actors_data[name] = request.json

    return make_response(jsonify(actors_data[name]), 201)


@app.route('/movies/add_movie', methods=['POST'])
def add_movie():
    """
    Add a new movie data
    :return: the new movie object
    """
    if not request.json or 'json_class' not in request.json or 'name' not in request.json \
            or 'wiki_page' not in request.json or 'box_office' not in request.json or 'year' not in request.json \
            or 'actors' not in request.json:
        abort(400)

    name = request.json['name']

    movies_data[name] = request.json

    return make_response(jsonify(movies_data[name]), 201)


@app.route('/actors/<string:actor_name>', methods=['DELETE'])
def delete_actor(actor_name):
    """
    Delete the input actor
    :param actor_name: the actor to delete
    :return: success message
    """
    actor_name = actor_name.replace('_', ' ')
    for actor in actors_data:
        if actor.lower() == actor_name.lower():
            del actors_data[actor]
            return make_response(jsonify({'Success': 'Deletion completed'}))

    abort(404)


@app.route('/movies/<string:movie_name>', methods=['DELETE'])
def delete_movie(movie_name):
    """
    Delete the input movie
    :param movie_name: the movie to delete
    :return: success message
    """
    movie_name = movie_name.replace('_', ' ')
    for movie in movies_data:
        if movie.lower() == movie_name.lower():
            del movies_data[movie]
            return make_response(jsonify({'Success': 'Deletion completed'}))

    abort(404)


@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 not found
    :return: the 404 not found response
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    with open('data.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

        actors_data = data[0]
        movies_data = data[1]

    app.run(debug=True)
