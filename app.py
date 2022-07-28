from flask import Flask
from cursos import blue_cursos
from login import blue_registro
from examenes import blue_examenes

app = Flask(__name__)
app.register_blueprint(blue_cursos,url_prefix="/cursos")
app.register_blueprint(blue_registro,url_prefix="/login")
app.register_blueprint(blue_examenes,url_prefix="/examenes")


@app.route('/')
@app.route("/index")
@app.route("/inicio")
def index():
    return "Bienvenido a nuestra app"

@app.route("/pruebas")
def pruebas():
    return "Bienvenido otra vez"

if __name__ == '__main__':
    app.run()#se puede cambiar el puerto con port

