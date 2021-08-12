#Importe de instancia de flask.
from src.app import app

#CONSTANTES DE CONFIGURACIÓN
HOST="localhost"
PORT=4000
DEBUG=True

#Arranque del proyecto.
if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)