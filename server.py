from flask import Flask, redirect, request, abort
from functools import wraps
import os


application = Flask(__name__)


def require_api_key(view_function):
    @wraps(view_function)
    def check_header_auth(*args, **kwargs):
        if request.headers["Authorization"] == os.environ['ACCESS_KEY']:
            return view_function(*args, **kwargs)
        else:
            print("Inadequate authorization supplied")
            abort(401)

    return check_header_auth


@application.route('/ping')
def home_page():
    """Health check route to ensure app is running."""
    return "pong", 201, {'Content-Type': 'text/html'}


@application.route('/train', methods = ['GET'])
def train_model():
    result = "Doing all the training"
    return result, 201, {'Content-Type': 'application/json'}


@application.route('/score', methods = ['GET'])
def score_model():
    result = "Amazing predictions for sure"
    return result, 201, {'Content-Type': 'application/json'}


if __name__ == "__main__":
    application.run()
