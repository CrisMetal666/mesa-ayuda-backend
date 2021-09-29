from app import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    clave = db.Column(db.String(150), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)

    def __init__(self, id, persona_id, clave, habilitado, usuario_id):
        self.id = id
        self.persona_id = persona_id
        self.clave = clave
        self.habilitado = habilitado
        self.usuario_id = usuario_id
