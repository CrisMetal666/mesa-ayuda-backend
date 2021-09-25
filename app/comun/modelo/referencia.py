from app import db


class Referencia(db.Model):
    __tablename__ = 'referencia'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(200), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    limite_contador = db.Column(db.Integer, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
