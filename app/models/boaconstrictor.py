from app.config.db import db

class BoaConstrictor(db.Model):
    __tablename__ = "boas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=False)
    ratones_comidos = db.Column(db.Integer, default=0, nullable=False)

    def hacer_sonido(self) -> str:
        return "¡Tsss!"

