from flask import Flask
from src.routes.public_routes import *

#Instancia de flask.
app = Flask(__name__)

app.add_url_rule(routes['index_route'], view_func=routes['index_controller'])
app.add_url_rule(routes['contact_route'], view_func=routes['contact_controller'])