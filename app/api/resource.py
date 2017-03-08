"""Module to test app is up and running."""
from app.api import api


@api.route("/")
def _congratulations():
    return "Congratulations! You have successfully launched your project"
