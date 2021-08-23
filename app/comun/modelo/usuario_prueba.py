from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.comun.validacion_campos import validar_obligatorio


class UsuarioPrueba(db.Model):
    MENSAJE_NOMBRE_OBLIGATORIO = 'Debe ingresar el nombre'
    MENSAJE_APELLIDO_OBLIGATORIO = 'Debe ingresar el apellido'
    MENSAJE_CORREO_OBLIGATORIO = 'Debe ingresar el correo'
    MENSAJE_CLAVE_OBLIGATORIO = 'Debe ingresar el clave'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    correo = db.Column(db.String)
    clave = db.Column(db.String)

    def __init__(self, id, nombre, apellido, correo, clave):
        validar_obligatorio(nombre, self.MENSAJE_NOMBRE_OBLIGATORIO)
        validar_obligatorio(apellido, self.MENSAJE_APELLIDO_OBLIGATORIO)
        validar_obligatorio(correo, self.MENSAJE_CORREO_OBLIGATORIO)
        validar_obligatorio(clave, self.MENSAJE_CLAVE_OBLIGATORIO)

        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = generate_password_hash(clave)

    def verificar_coincidencia_clave(self, clave):
        return check_password_hash(self.clave, clave)
