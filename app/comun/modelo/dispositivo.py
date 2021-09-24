from app import db


class Dispositivo(db.Model):
    __tablename__ = 'dispositivo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial = db.Column(db.String(200), nullable=False)
    referencia_id = db.Column(db.Integer, db.ForeignKey('referencia.id'), nullable=False)
    tipo_dispositivo = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
