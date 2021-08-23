from app.comun.modelo.usuario_prueba import UsuarioPrueba


class FabricaUsuario:
    def crear(self, comando_usuario):
        return UsuarioPrueba(
            id=comando_usuario['id'],
            nombre=comando_usuario['nombre'],
            apellido=comando_usuario['apellido'],
            correo=comando_usuario['correo'],
            clave=comando_usuario['clave']
        )
