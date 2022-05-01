from datetime import datetime
import logging

from utils.collect import collect_data
from utils.process import preprocessing
from utils.io import load_model_object

def prediction_workload(**kwargs):
    print(f"Prediction workload initiated at {str(datetime.utcnow())[0:19]}")
    logging.info(f"Prediction workload initiated at {str(datetime.utcnow())[0:19]}")
    ## Fetch data
    ## Caching
    ## Preprocessing
    ##  - Valuable to have a preprocessing function that can
    ##      apply the same transformations to the data in both
    ##      training and prediction
    ## Load model
    ## Generate predictions
    ## Return/store predictions

    data = collect_data(scenario = 'prediction')
    data = preprocessing(data)

    filename = "Great model"
    model = load_model_object(filename)
    predictions = model.predict(data)
    logging.info("""
    Message describing prediction characteristics, such as duration of the function
    or the class distribution of the predictions.
    """)
    return "Great predictions"