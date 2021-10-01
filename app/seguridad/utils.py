from flask_jwt_extended import get_jwt


def obtener_usuario_id():
    return get_jwt()['usuario_id']
