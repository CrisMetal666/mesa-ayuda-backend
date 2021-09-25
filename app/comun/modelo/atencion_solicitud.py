from app import db


class AtencionSolicitud(db.Model):
    __tablename__ = 'atencion_solicitud'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    solicitud_servicio_id = db.Column(db.Integer, db.ForeignKey('solicitud_servicio.id'), nullable=False)
    fecha_asignacion = db.Column(db.DateTime, nullable=False)
    tecnico_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    descripcion_solucion = db.Column(db.String(300))
    fecha_realizacion = db.Column(db.DateTime)
    usuario_id = db.Column(db.Integer, nullable=False)
