from app.comun.modelo.persona import Persona
from app.comun.modelo.role import Role
from app.comun.modelo.usuario import Usuario
from app.comun.modelo.usuario_role import UsuarioRole


class DaoInicioSesion:

    def buscar_usuario_por_identificacion(self, identificacion):
        return Usuario.query.join(Persona, Usuario.persona_id == Persona.id).filter_by(identificacion=identificacion). \
            first()

    def buscar_role_por_usuario(self, usuario_id):
        return Role.query.join(UsuarioRole, Role.id == UsuarioRole.role_id).filter_by(usuario_id=usuario_id).all()
