#!/usr/bin/python3
""" api view route"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_route():
    """route to check status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ This endpoint retrieves the number of each object by type """

    obj = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
    obj_names = ["amenities", "cities", "places", "reviews", "states", "users"]

    obj_dict = {obj_names[i]: storage.count(obj[i]) for i in range(len(obj))}

    return jsonify(obj_dict)
