## Placeholder for data collection function(s)

## Ideally, the model has a single data source to use in train and
## prediction scenarios (often not the case) as well as a single
## collection function that retrieves the data in a unified way
## to minimize training/prediction skew.

import logging


def collect_data(**kwargs):
    """
    Ideally, a function that defines how data should be collected 
    for training and prediction.

    In the real world, of course, there are often differences in data
    sources between training (data warehouse) and prediction (production
    application database, streaming system) scenarios. In such cases, one 
    option would be to handle training/prediction scenarios as a positional, 
    named, or keyword argument with control logic to determine how to
    collect the data from the relevant system. A second option would be to
    create and maintain to distinct functions. I generally prefer a single
    function with a keyword argument and control logic.

    Even if training and prediction data are originating from the same
    data source, you likely need control logic to handle filtering the data
    correctly in each of those scenarios (e.g., give me all the data for the
    last two years to train vs. just the data for the last hour to predict).
    """

    ## Control logic assumes prediction is the default scenario
    if kwargs.get('scenario') == 'training':
        data = "Retrieve the training data from the historical data source with relevant filter"
    else:
        data = "Retrieve the prediction data from the real-time source with relevant filter"
    logging.info(f"Logging describing the data, such as its size in memory or number of records")
    return data
