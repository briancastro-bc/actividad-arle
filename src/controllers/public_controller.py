from flask import render_template, flash, request, redirect, url_for
from flask.views import MethodView
from src.db import *

class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            try:
                cur.execute("SELECT titulo, descripcion, fechaLimite, imagen FROM anuncios")
                announcements = cur.fetchall()
            except:
                flash("Un error ha ocurrido mientras intentabamos mostrar los datos", "error")
            return render_template('views/index.html', announcements=announcements)

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