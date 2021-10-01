from app.comun.esquema.esquema_detalle import EsquemaDetalle


class ServicioConsultarPorMaestro:

    def __init__(self, dao_detalle):
        self.dao_detalle = dao_detalle

    def ejecutar(self, maestro_id):
        detalles = self.dao_detalle.obtener_por_maestro_id(maestro_id)
        esquema_detalle = EsquemaDetalle(many=True)
        return esquema_detalle.dump(detalles)
