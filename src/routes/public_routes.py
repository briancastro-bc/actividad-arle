from src.controllers.public_controller import *

routes = {
    "index_route": "/", "index_controller": IndexController.as_view('index'),
    "announcements_route": "/announcements", "announcements_controller": AnnouncementsController.as_view('Announcements'),
    "categories_route": "/categories", "categories_controller": CategoriesController.as_view('Categories')
}