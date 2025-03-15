from flask import Blueprint, jsonify,render_template
from flask import Response
import json
from app.models.boaconstrictor import BoaConstrictor
from app.models.gato import Gato
from app.models.perro import Perro
from app.models.huron import Huron

animal_bp = Blueprint("animal_bp", __name__)

@animal_bp.route("/")
def vista_animales():
    return render_template("animales.html", 
                           gato=Gato().hacer_sonido(),
                           perro=Perro().hacer_sonido(),
                           huron=Huron().hacer_sonido(),
                           boa=BoaConstrictor().hacer_sonido())

@animal_bp.route("/api/animal/sonido/perro", methods=["GET"])
def sonido_perro():
    return jsonify({"animal": "Perro", "sonido": Perro().hacer_sonido()})

@animal_bp.route("/api/animal/sonido/huron", methods=["GET"])
def sonido_huron():
    sonido = Huron().hacer_sonido()
    return Response(
        json.dumps({"animal": "Hurón", "sonido": sonido}, ensure_ascii=False),
        mimetype="application/json",
        status=200
    )

@animal_bp.route("/api/animal/sonido/gato", methods=["GET"])
def sonido_gato():
    return jsonify({"animal": "Gato", "sonido": Gato().hacer_sonido()})

@animal_bp.route("/api/animal/sonido/boa", methods=["GET"])
def sonido_boa():
    sonido = BoaConstrictor().hacer_sonido()
    return Response(
        json.dumps({"animal": "Boa Constrictor", "sonido": sonido}, ensure_ascii=False),
        mimetype="application/json",
        status=200
    )