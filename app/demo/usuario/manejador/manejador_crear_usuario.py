from app.comun.comando_respuesta import ComandoRespuesta


class ManejadorCrearUsuario:

    def __init__(self, fabrica_usuario, servicio_crear_usuario):
        self.fabrica_usuario = fabrica_usuario
        self.servicio_crear_usuario = servicio_crear_usuario

    def ejecutar(self, comando_usuario):
        usuario = self.fabrica_usuario.crear(comando_usuario)
        respuesta = self.servicio_crear_usuario.ejecutar(usuario)
        return ComandoRespuesta(respuesta)
