import joblib


def cache_model_object(model):
    """
    Function to store the model object in an appropriate place.

    In this sample, we'll store the model object locally. In the real world,
    this would be considered a bad practice, mainly because model binaries
    should not be stored in a public-facing repository like GitHub.

    The right pattern for this is to store the model object in an artifact
    repository or a storage bucket.
    """
    joblib.dump(model, 'model') ## Replace this code with something sensible.
    return "Wrote the model locally, which is definitely not the right choice."
