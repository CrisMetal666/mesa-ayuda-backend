from app import db


class Sede(db.Model):
    __tablename__ = 'sede'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(200), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    principal = db.Column(db.Boolean, nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
