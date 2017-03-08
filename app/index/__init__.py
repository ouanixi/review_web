"""BluePrint creator."""
from flask import Blueprint

ind = Blueprint("index", __name__, url_prefix="/")

from app.index import resource  # noqa
