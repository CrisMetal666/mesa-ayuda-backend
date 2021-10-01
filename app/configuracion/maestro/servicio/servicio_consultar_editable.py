from app.comun.esquema.esquema_maestro import EsquemaMaestro


class ServicioConsultarEditable:

    def __init__(self, dao_maestro):
        self.dao_maestro = dao_maestro

    def ejecutar(self):
        maestros = self.dao_maestro.obtener_editables()
        esquema_maestro = EsquemaMaestro(many=True)
        return esquema_maestro.dump(maestros)
