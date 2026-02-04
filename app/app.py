from flask import Flask, request, jsonify
from .database import init_db
from .models import crear_orden, listar_ordenes, actualizar_estado

app = Flask(__name__)

@app.route("/orden", methods=["POST"])
def crear():
    data = request.json
    crear_orden(data["cliente"], data["descripcion"])
    return jsonify({"mensaje": "Orden creada correctamente"}), 201

@app.route("/orden", methods=["GET"])
def listar():
    ordenes = listar_ordenes()
    resultado = []
    for o in ordenes:
        resultado.append({
            "id": o[0],
            "cliente": o[1],
            "descripcion": o[2],
            "estado": o[3]
        })
    return jsonify(resultado)

@app.route("/orden/<int:orden_id>", methods=["PUT"])
def actualizar(orden_id):
    data = request.json
    actualizar_estado(orden_id, data["estado"])
    return jsonify({"mensaje": "Estado actualizado"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
