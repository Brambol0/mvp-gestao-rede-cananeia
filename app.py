
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Sistema de Gestão - Rede Cananéia"

if __name__ == "__main__":
    app.run(debug=True)
