from app.comun.excepciones import ExcepcionCampoInvalido


class ServicioCrearDetalle:
    MENSAJE_DETALLE_NO_PUEDE_TENER_ID = 'El detalle no puede tener id'

    def __init__(self, repositorio_detalle):
        self.repositorio_detalle = repositorio_detalle

    def ejecutar(self, detalle):
        if detalle.id:
            raise ExcepcionCampoInvalido(self.MENSAJE_DETALLE_NO_PUEDE_TENER_ID)

        return self.repositorio_detalle.guardar(detalle)
