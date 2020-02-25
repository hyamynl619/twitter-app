""" Entry point for app """

from .hello import create_app

APP = create_app
APP.run(debug=True)