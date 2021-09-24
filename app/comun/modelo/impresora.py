from app import db


class Impresora(db.Model):
    __tablename__ = 'impresora'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_contador = db.Column(db.Date, nullable=False)
    contador = db.Column(db.Integer, nullable=False)
    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id'), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
