from app import create_app
from app.config.config import Config
from app.config.db import db
from app.controllers.home_controller import animal_bp

app = create_app(Config)

def register_routes(app):
    app.register_blueprint(animal_bp)

register_routes(app)  # ✅ Ahora sí registra las rutas