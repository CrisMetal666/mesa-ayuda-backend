from app import db


class Empresa(db.Model):
    __tablename__ = 'empresa'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_identificacion_id = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    identificacion = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(200), nullable=False)
    correo = db.Column(db.String(200), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
