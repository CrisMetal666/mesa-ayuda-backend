from app.comun.comando_respuesta import ComandoRespuesta
from app.comun.esquema.esquema_comando_respuesta import EsquemaComandoRespuesta
from app.seguridad.utils import obtener_usuario_id


class ManejadorCrearDetalle:

    def __init__(self, fabrica_detalle, servicio_crear_detalle):
        self.fabrica_detalle = fabrica_detalle
        self.servicio_crear_detalle = servicio_crear_detalle

    def ejecutar(self, comando_detalle):
        comando_detalle['usuario_id'] = obtener_usuario_id()
        detalle = self.fabrica_detalle.crear(comando_detalle)
        resultado = self.servicio_crear_detalle.ejecutar(detalle)
        esquema_comando_respuesta = EsquemaComandoRespuesta()
        return esquema_comando_respuesta.dump(ComandoRespuesta(resultado))
