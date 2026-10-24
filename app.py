
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Sistema de Gestão - Rede Cananéia"


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


if __name__ == "__main__":
    app.run(debug=True)
