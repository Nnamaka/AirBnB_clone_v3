#!/usr/bin/python3
"""State view for state objects"""
from api.v1.views import app_views
from flask import request, abort, jsonify, make_response
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """ gets the list of all states object """
    states = storage.all(State).values()
    state_list = []

    for state in states:
        state_list.append(state.to_dict())

    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def a_state(state_id):
    """ gets a state object """
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_a_state(state_id):
    """ deletes a state object """
    state = storage.get(State, state_id)

    if not state:
        abort(404)
    storage.delete(state)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ create a state object """
    if type(request.get_json()) != dict:
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description='Missing name')

    state = request.get_json()
    instance = State(**state)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ update a state object """
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    if not request.get_json():
        abort(400, description='Not a JSON')

    state = request.get_json()
    for k, v in dtate.items():
        if k not in ['created_at', 'id', 'updated_at']:
            setattr(state, k, v)

    storage.save()

    return make_response(jsonify(state.to_dict()), 200)
