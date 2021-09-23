from app import db


class UsuarioRole(db.Model):
    __tablename__ = 'usuario_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
