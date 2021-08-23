class ServicioCrearUsuario:

    def __init__(self, repositorio_usuario):
        self.repositorio_usuario = repositorio_usuario

    def ejecutar(self, usuario):
        return self.repositorio_usuario.crear(usuario)
