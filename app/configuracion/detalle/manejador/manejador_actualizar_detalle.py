from app.comun.comando_respuesta import ComandoRespuesta
from app.comun.esquema.esquema_comando_respuesta import EsquemaComandoRespuesta
from app.comun.esquema.esquema_detalle import EsquemaDetalle
from app.seguridad.utils import obtener_usuario_id


class ManejadorActualizarDetalle:

    def __init__(self, fabrica_detalle, servicio_actualizar_detalle):
        self.fabrica_detalle = fabrica_detalle
        self.servicio_actualizar_detalle = servicio_actualizar_detalle

    def ejecutar(self, comando_detalle):
        comando_detalle['usuario_id'] = obtener_usuario_id()
        detalle = self.fabrica_detalle.crear(comando_detalle)
        resultado = self.servicio_actualizar_detalle.ejecutar(detalle)
        return self._contruir_respuesta(resultado)

    def _contruir_respuesta(self, resultado):
        esquema_comando_respuesta = EsquemaComandoRespuesta()
        esquema_detalle = EsquemaDetalle()
        dump_detalle = esquema_detalle.dump(resultado)
        return esquema_comando_respuesta.dump(ComandoRespuesta(dump_detalle))
