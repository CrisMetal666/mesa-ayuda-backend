from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.comun.excepciones import ExcepcionCredencialesIncorrectas, ExcepcionSinAutorizacion


class ServicioInicioSesion:
    MENSAJE_USUARIO_NO_ENCONTRADO = 'Usuario no encontrado'
    MENSAJE_CLAVE_INVALIDA = 'Contraseña incorrecta'
    MENSAJE_SIN_ROLE_ASIGNADO = 'El usuario no tiene roles asignados'
    MENSAJE_USUARIO_INHABILITADO = 'El usuario se encuntra inhabilitado'

    def __init__(self, dao_inicio_sesion):
        self.dao_inicio_sesion = dao_inicio_sesion

    def ejecutar(self, identificacion, clave):
        usuario = self._buscar_y_validar_usuario(identificacion, clave)
        roles = self._buscar_y_validar_roles(usuario.id)
        return self._generar_token(identificacion, usuario.id, roles)

    def _generar_token(self, identificacion, usuario_id, roles):
        informacion_adicional = {'usuario_id': usuario_id, 'authorities': roles}
        token = create_access_token(identity=identificacion, additional_claims=informacion_adicional)
        return token

    def _buscar_y_validar_usuario(self, identificacion, clave):
        usuario = self.dao_inicio_sesion.buscar_usuario_por_identificacion(identificacion)

        if usuario is None:
            raise ExcepcionCredencialesIncorrectas(self.MENSAJE_USUARIO_NO_ENCONTRADO)

        if not check_password_hash(usuario.clave, clave):
            raise ExcepcionCredencialesIncorrectas(self.MENSAJE_CLAVE_INVALIDA)

        if not usuario.habilitado:
            raise ExcepcionSinAutorizacion(self.MENSAJE_USUARIO_INHABILITADO)

        return usuario

    def _buscar_y_validar_roles(self, usuario_id):
        roles = self.dao_inicio_sesion.buscar_role_por_usuario(usuario_id)

        if len(roles) == 0:
            raise ExcepcionSinAutorizacion(self.MENSAJE_SIN_ROLE_ASIGNADO)

        roles_formateado = []

        for role in roles:
            roles_formateado.append(role.nombre)

        return roles_formateado
