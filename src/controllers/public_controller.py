from flask import render_template, flash
from flask.views import MethodView

class IndexController(MethodView):
    def get(self):
        return "Hello World!"

class ContactController(MethodView):
    def get(self):
        return "Contact controller is works!"

    def post(self):
        pass