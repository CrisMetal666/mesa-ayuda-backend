from app.comun.esquema.esquema_detalle import EsquemaDetalle
from app.comun.excepciones import ExcepcionEntidadNoEncontrada


class ServicioConsultarPorId:
    MENSAJE_DETALLE_NO_ENCONTRADO = 'No existe el detalle solicitado'

    def __init__(self, dao_detalle):
        self.dao_detalle = dao_detalle

    def ejecutar(self, id):
        detalle = self.dao_detalle.obtener_por_id(id)

        if detalle is None:
            raise ExcepcionEntidadNoEncontrada(self.MENSAJE_DETALLE_NO_ENCONTRADO)

        esquema_detalle = EsquemaDetalle(many=False)
        return esquema_detalle.dump(detalle)
