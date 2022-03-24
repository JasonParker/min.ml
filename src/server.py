from flask import Flask, request, abort
from functools import wraps
import os

from modeling.predict import prediction_workload
from modeling.train import training_workload

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
    result = training_workload()
    return result, 201, {'Content-Type': 'text/html'}


@application.route('/predict', methods = ['GET'])
def predict_model():
    result = prediction_workload()
    return result, 201, {'Content-Type': 'text/html'}


if __name__ == "__main__":
    application.run()
