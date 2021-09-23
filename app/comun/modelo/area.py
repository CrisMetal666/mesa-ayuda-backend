from app import db


class Area(db.Model):
    __tablename__ = 'area'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(200), nullable=False)
    sede_id = db.Column(db.Integer, db.ForeignKey('sede.id'), nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
