#!/usr/bin/python3
"""amenities view that handle amenities objects"""
from api.v1.views import app_views
from flask import request, abort, jsonify, make_response
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """get amenities"""
    amenities = storage.all(Amenity).values()

    list_amenits = []

    for amenity in amenities:
        list_amenits.append(amenity.to_dict())

    return jsonify(list_amenits)


@app_views.route('/amenities/<amenity_id>/', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """get amenity"""
    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """delete amenity object"""

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    storage.delete(amenity)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """create amenity"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    req = request.get_json()
    obj = Amenity(**req)
    obj.save()

    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """update amenity"""

    if not request.get_json():
        abort(400, description="Not a JSON")

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    req = request.get_json()

    for k, v in req.items():
        if k not in ignore:
            setattr(amenity, k, v)
    storage.save()

    return make_response(jsonify(amenity.to_dict()), 200)
