from datetime import datetime

from data.collect import collect_data
from data.process import preprocessing


def prediction_workload(**kwargs):
    print(f"Prediction workload initiated at {str(datetime.utcnow())[0:19]}")
    ## Fetch data
    ## Splitting/caching
    ## Preprocessing
    ##  - Valuable to have a preprocessing function that can
    ##      apply the same transformations to the data in both
    ##      training and prediction
    ## Train model
    ## Evaluate
    ## Store model artifacts

    data = collect_data(scenario = 'prediction')
    data = preprocessing(data)
    
    return "Great predictions"