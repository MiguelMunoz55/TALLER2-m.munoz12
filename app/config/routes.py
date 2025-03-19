
from app.config.db import db
from app.controllers.home_controller import animal_bp


def register_routes(app):
    app.register_blueprint(animal_bp)

  # ✅ Ahora sí registra las rutas