from flask import render_template, flash
from flask.views import MethodView

class IndexController(MethodView):
    def get(self):
        return "Hello World!"

class AnnouncementsController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            title = []
            description = []

            
    def post(self):
        pass