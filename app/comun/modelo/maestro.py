from app import db


class Maestro(db.Model):
    __tablename__ = 'maestro'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    editable = db.Column(db.Boolean, nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
