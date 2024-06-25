from flask import Flask, jsonify, request, render_template
from Models import db, usuarios
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/au")
def addusr():
    return render_template("index.html")

@app.route("/searchRUT")
def searchRUT():
    return render_template("buscarRUT.html")



#funciones

@app.route("/list", methods=["GET"])
def Listar():
    try:
        User = usuarios.query.all()
        ListaReturn = [usuarios.serial() for usuarios in User]
        return jsonify(ListaReturn), 200
    except Exception:
        exception("[SERVER]: Error --->")
        return jsonify("Ha ocurrido un error :("), 500

    return "<h1>xxxx</h1>"





#FUNCION PARA AGREGAR USER
@app.route("/addUser", methods=["POST"])
def addUser():
     try:
          name = request.form["name"]
          apellido = request.form["apellido"]
          rut = request.form["rut"]

          user = usuarios(name, apellido, int(rut))
          db.session.add(user)
          db.session.commit()

          return jsonify(user.serial()), 200

     except Exception:
         exception("[SERVER]: Error --->")
         return jsonify({"Ha ocurrido un error :("}), 500
     return "<h1>Al menos esto salió</h1>"



#FUNCION PARA BUSCAR POR RUT
@app.route("/sRUT", methods=["POST"])
def sRUT():
    try:
        rutUser = request.form["rut"]

        RUT = usuarios.query.filter_by(rut=rutUser).first()
        if not RUT:
            return jsonify("no existe el user :(")
        else:
            return jsonify(RUT.serial()), 200

    except Exception:
        exception("[SERVER]: Error --->")
        return jsonify({"Ha ocurrido un error :("}), 500
    return "<h1>Al menos esto salió</h1>"


if __name__ == "__main__":
    app.run(port=5800)
