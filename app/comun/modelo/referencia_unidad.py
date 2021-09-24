from app import db


class ReferenciaUnidad(db.Model):
    __tablename__ = 'referencia_unidad'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_unidad = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    referencia_id = db.Column(db.Integer, db.ForeignKey('referencia.id'), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
