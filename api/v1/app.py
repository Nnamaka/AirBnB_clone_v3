#!/usr/bin/python3
"""main file """
from flask import Flask, jsonify, make_response
import os
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(error):
    """ handler returns 404 in json format """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    """code starts here"""
    api_host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    api_port = os.environ.get('HBNB_API_PORT', 5000)
    app.run(host=str(api_host), port=int(api_port), threaded=True)
