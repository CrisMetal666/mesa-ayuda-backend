from functools import wraps

from flask_jwt_extended import get_jwt

from app.seguridad.excepciones import ExcepcionSinAutorizacion

ROLE_ADMIN = 'ROLE_ADMIN'


def admin_requerido(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        validar_role_permitidos([ROLE_ADMIN])
        return f(*args, **kws)

    return decorated_function


def validar_role_permitidos(roles_permitido):
    roles_token = get_jwt()["authorities"]
    autorizado = False
    for role_token in roles_token:
        for role_permitido in roles_permitido:
            if role_token == role_permitido:
                autorizado = True

    if not autorizado:
        raise ExcepcionSinAutorizacion('No tiene permisos para consultar el recurso solicitado')
