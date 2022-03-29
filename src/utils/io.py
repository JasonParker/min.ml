import joblib


def cache_model_object(model, filename):
    """
    Function to store the model object in an appropriate place.

    In this sample, we'll store the model object locally. In the real world,
    this would be considered a bad practice, mainly because model binaries
    should not be stored in a public-facing repository like GitHub.

    The right pattern for this is to store the model object in an artifact
    repository or a storage bucket.
    """
    joblib.dump(model, filename) ## Replace this code with something sensible.
    return f"Wrote the model locally to '{filename}', which is definitely not the right choice."


def load_model_object(filename):
    """
    Function to fetch the model object from an appropriate place.

    Same caveats as cache_model_object: don't store your model object locally,
    use an artifact registry or storage bucket and write sensible code to retrieve it here.
    """
    model = joblib.load(filename)
    return model