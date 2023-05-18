#!/usr/bin/python3
""" api view route"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_route():
    """route to check status"""
    return jsonify({"status": "OK"})
