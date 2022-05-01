from datetime import datetime
import logging

from utils.collect import collect_data
from utils.process import preprocessing
from utils.io import cache_model_object


def training_workload(**kwargs):
    print(f"Training workload initiated at {str(datetime.utcnow())[0:19]}")
    logging.info(f"Training workload initiated at {str(datetime.utcnow())[0:19]}")
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

    model = "Great model"
    filename = "Great model"
    modelCachingMsg = cache_model_object(model, filename)
    print(modelCachingMsg)
    
    return "Great model"