from app import db
from app.comun.validacion_campos import validar_obligatorio, validar_longitud


class Detalle(db.Model):
    MENSAJE_VALOR_LONGITUD = 'El valor no puede tener más de 200 carácteres'
    MENSAJE_MAESTRO_OBLIGATORIO = 'Debe ingresar el maestro'
    MENSAJE_HABILITADO_OBLIGATORIO = 'Debe ingresar si está habilitado'
    MENSAJE_USUARIO_OBLIGATORIO = 'Debe ingresar el usuario id'

    __tablename__ = 'detalle'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.String(200), nullable=False)
    maestro_id = db.Column(db.Integer, db.ForeignKey('maestro.id'), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)

    def __init__(self, id, valor, maestro_id, habilitado, usuario_id):
        validar_longitud(valor, 200, self.MENSAJE_VALOR_LONGITUD)
        validar_obligatorio(maestro_id, self.MENSAJE_MAESTRO_OBLIGATORIO)
        validar_obligatorio(habilitado, self.MENSAJE_HABILITADO_OBLIGATORIO)
        validar_obligatorio(usuario_id, self.MENSAJE_USUARIO_OBLIGATORIO)

        self.id = id
        self.valor = valor
        self.maestro_id = maestro_id
        self.habilitado = habilitado
        self.usuario_id = usuario_id
