from app.config.db import db

class Gato(db.Model):
    __tablename__ = "gatos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=False)
    raza = db.Column(db.String(45), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Numeric, nullable=False)

    def hacer_sonido(self) -> str:
        return "Miau Miau"
