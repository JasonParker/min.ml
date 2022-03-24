from datetime import datetime
import joblib

from src.data.collect import collect_data
from src.data.process import preprocessing


def training_workload(**kwargs):
    ## Fetch data
    ## Splitting/caching
    ## Preprocessing
    ##  - Valuable to have a preprocessing function that can
    ##      apply the same transformations to the data in both
    ##      training and prediction
    ## Train model
    ## Evaluate
    ## Store model artifacts

    data = collect_data(scenario = 'training')
    data = preprocessing(data)
    
    return "Great model"