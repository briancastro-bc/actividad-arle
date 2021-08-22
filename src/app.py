from flask import Flask, render_template
from src.routes.public_routes import *

#Instancia de flask.
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="ASBDNnlajkbdasdjvbOYIVASDJVHA"
)

app.add_url_rule(routes['index_route'], view_func=routes['index_controller'])
app.add_url_rule(routes['announcements_route'], view_func=routes['announcements_controller'])
app.add_url_rule(routes['categories_route'], view_func=routes['categories_controller'])