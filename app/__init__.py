from flask import Flask
from app.config.config import Config
from app.config.db import db
from app.config.routes import register_routes

def create_app():
    app = Flask(__name__, template_folder="views")

    app.config.from_object(Config)

    # 🔥 Agrega este print para ver si la variable se carga
    print("DATABASE_URI en Render:", app.config.get("SQLALCHEMY_DATABASE_URI"))

    if not app.config.get("SQLALCHEMY_DATABASE_URI"):
        raise RuntimeError("SQLALCHEMY_DATABASE_URI no está definida.")

    db.init_app(app)
    register_routes(app)

    return app