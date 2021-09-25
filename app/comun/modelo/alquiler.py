from app import db


class Alquiler(db.Model):
    __tablename__ = 'alquiler'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id'), nullable=False)
    sede_id = db.Column(db.Integer, db.ForeignKey('sede.id'), nullable=False)
    fecha_cohorte = db.Column(db.Date, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
