## Placeholder for data processing functions

## Preprocessing
## Feature engineering
## Normalization/scaling

## The goal is to call the same data processing functions
## for both training and prediction prediction to minimize
## risk of skew between those scenarios.

import logging


def preprocessing(data):
    result = """Recommend having a workload function that 
    calls more modular functions to execute preprocessing, feature
    engineering, and normalization steps. """

    logging.info("""
    Message describing preprocessing, such as the duration of the function call,
    distribution of missing or outlier values, number of records where imputation
    was applied, and other details about transformations.

    When debugging a machine learning model, you'll never wish you had less 
    information about these kinds of things.
    """)
    return result 