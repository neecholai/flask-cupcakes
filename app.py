"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request
from models import db, connect_db, Cupcake, default_image
from flask_debugtoolbar import DebugToolbarExtension
from serializers import cupcake_serializer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'whatever'

toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.route('/api/cupcakes')
def list_cupcakes():
    """ Return JSON obj {cupcakes: [{id, flavor, size,
     rating, image}, ...]} """

    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [cupcake_serializer(cupcake) for cupcake in cupcakes]

    return jsonify(cupcakes=serialized_cupcakes)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """ Return JSON obj {cupcake: {id, flavor, size, rating, image}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake_serializer(cupcake)

    return jsonify(cupcake=serialized_cupcake)


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """
    Return JSON obj {cupcake: {id, flavor, size, rating, image}}
    """

    cupcake_data = {'flavor': request.json.get('flavor'),
                    'size': request.json.get('size'),
                    'rating': request.json.get('rating'),
                    'image': request.json.get('image') or None}

    new_cupcake = Cupcake(**cupcake_data)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = cupcake_serializer(new_cupcake)

    return (jsonify(cupcake=serialized_cupcake), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """
    Update cupcake and return JSON obj {cupcake: {id, flavor, size,
    rating, image}}
    """

    updated_cupcake = Cupcake.query.get_or_404(cupcake_id)

    updated_cupcake.flavor = request.json.get('flavor'),
    updated_cupcake.size = request.json.get('size'),
    updated_cupcake.rating = request.json.get('rating'),
    updated_cupcake.image = request.json.get('image') or default_image

    db.session.commit()

    serialized_updated_cupcake = cupcake_serializer(updated_cupcake)

    return jsonify(cupcake=serialized_updated_cupcake)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """ Delete cupcake and return JSON obj {message: "Deleted"}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    message = "Deleted"

    return jsonify(message=message)
