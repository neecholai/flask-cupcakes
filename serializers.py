def cupcake_serializer(cupcake):
    """ Serialize a cupcake SQLAlchemy to dictionary"""

    return {
        'id': cupcake.id,
        'flavor': cupcake.flavor,
        'size': cupcake.size,
        'rating': cupcake.rating,
        'image': cupcake.image
    }