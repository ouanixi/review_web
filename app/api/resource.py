from app.api import api


@api.route("/")
def congratulations():
    return "Congratulations! You have successfully launched your project"
