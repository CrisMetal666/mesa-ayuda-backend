from app import db


class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identificacion = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(10), nullable=False)
    apellido = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(200), nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
