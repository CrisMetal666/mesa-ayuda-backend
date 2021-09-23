from app import db


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(20), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
