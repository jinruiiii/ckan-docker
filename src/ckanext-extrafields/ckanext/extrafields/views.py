from flask import Blueprint


extrafields = Blueprint(
    "extrafields", __name__)


def page():
    return "Hello, extrafields!"


extrafields.add_url_rule(
    "/extrafields/page", view_func=page)


def get_blueprints():
    return [extrafields]
