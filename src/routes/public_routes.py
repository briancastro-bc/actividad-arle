from src.controllers.public_controller import *

routes = {
    "index_route": "/", "index_controller": IndexController.as_view('index'),
    "contact_route": "/contact", "contact_controller": ContactController.as_view('contact')
}