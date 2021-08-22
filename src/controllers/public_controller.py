from flask import render_template, flash, request, redirect, url_for
from flask.views import MethodView
from pymysql import DBAPISet
from src.db import *

class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            try:
                cur.execute("SELECT titulo, descripcion, fechaLimite, imagen FROM anuncios")
                announcements = cur.fetchall()
                cur.execute("SELECT nombre, descripcion, imagen FROM categorias")
                categories = cur.fetchall()
            except:
                flash("Un error ha ocurrido mientras intentabamos mostrar los datos", "error")
            return render_template('views/index.html', announcements=announcements, categories=categories)

class AnnouncementsController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            title = []
            description = []

            
    def post(self):
        title = request.form['titulo']
        description = request.form['descripcion']
        image = request.form['imagen']
        limit_date = request.form['fechaLimite']
        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO anuncios(titulo, descripcion, fechaLimite, imagen) VALUES(%s, %s, %s, %s)", (title, description, limit_date, image))
                cur.connection.commit()
                flash("El anuncio ha sido creado correctamente", "success")
            except Exception as e:
                flash(f"{e}", "error")
            return redirect(url_for('index'))

#PENDIENTE

# class ModifyAnnouncementsController(MethodView):
    
#     def get(self): 
#         title = []
#         description = []

#     def post(self):
#         db = pymysql.connect("localhost","root","","anuncios")
#         cur_update = db.cursor()
#         title = request.form['newTitulo']
#         description = request.form['descripcion']
#         image = request.form['imagen']
#         limit_date = request.form['fechaLimite']

#         sql_update = "update anuncios set titulo = '%s' where new_titulo = '%s'"

#         with mysql.cursor() as cur:
#             try:
#                 cur_update.execute(sql_update % "new_title", "new_user_id")
#                 db.commit()
#                 flash("El anuncio ha sido creado correctamente", "success")
#             except Exception as e:
#                 flash(f"{e}", "error")
#             return redirect(url_for('index'))

class CategoriesController(MethodView): 
    
    def get(self):
        with mysql.cursor() as cur:
            name = []
            description = []

    def post(self):
        name = request.form['nombre']
        description = request.form['descripcionCat']
        image = request.form['imagenCat']
        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO categorias(nombre, descripcion, imagen) VALUES(%s, %s, %s)", (name, description, image))
                cur.connection.commit()
                flash("La categoría ha sido creado correctamente", "success")
            except Exception as e:
                flash(f"{e}", "error")
            return redirect(url_for('index'))