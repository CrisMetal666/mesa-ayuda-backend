from app import db


class ImpresoraUnidad(db.Model):
    __tablename__ = 'impresora_unidad'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    impresora_id = db.Column(db.Integer, db.ForeignKey('impresora.id'), nullable=False)
    unidad_id = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    contador = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
