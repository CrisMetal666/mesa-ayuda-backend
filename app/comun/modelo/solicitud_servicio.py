from app import db


class SolicitudServicio(db.Model):
    __tablename__ = 'solicitud_servicio'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    radicado = db.Column(db.String(100), nullable=False)
    fecha_solicitud = db.Column(db.Date, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'), nullable=False)
    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id'))
    solicitante = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    tipo_solicitud_id = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    descripcion_requerimiento = db.Column(db.String(300), nullable=False)
    tipo_cliente_id = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    recibio_solicitud_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    medio_solicitud_id = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('detalle.id'), nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)

