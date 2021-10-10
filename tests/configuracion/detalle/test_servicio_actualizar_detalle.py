from unittest.mock import MagicMock

from app.comun.excepciones import ExcepcionCampoInvalido, ExcepcionEntidadNoEncontrada
from app.configuracion.detalle.repositorio.repositorio_detalle import RepositorioDetalle
from app.configuracion.detalle.servicio.servicio_actualizar_detalle import ServicioActualizarDetalle
from tests import ClaseBaseTest
from tests.comun.constructor.constructor_detalle import ConstructorDetalle

repositorio_detalle = RepositorioDetalle()
servicio_actualizar_detalle = ServicioActualizarDetalle(repositorio_detalle)


class TestServicioActualizarDetalle(ClaseBaseTest):

    def test_detalle_sin_id(self):
        detalle = ConstructorDetalle.id(None).construir()

        with self.assertRaises(ExcepcionCampoInvalido) as cm:
            servicio_actualizar_detalle.ejecutar(detalle)

        self.assertEqual(servicio_actualizar_detalle.MENSAJE_DETALLE_SIN_ID, str(cm.exception))

    def test_detalle_no_existe(self):
        detalle = ConstructorDetalle.id(100).construir()
        repositorio_detalle.buscar_por_id = MagicMock(return_value=None)

        with self.assertRaises(ExcepcionEntidadNoEncontrada) as cm:
            servicio_actualizar_detalle.ejecutar(detalle)

        self.assertEqual(servicio_actualizar_detalle.MENSAJE_ENTIDAD_NO_ENCONTRADA, str(cm.exception))

    def test_datos_correctos(self):
        detalle_id = 55
        valor = 'Nuevo valor'
        maestro_id = 4
        habilitado = 0
        usuario_id = 3
        detalle = ConstructorDetalle.id(detalle_id).valor(valor).maestro_id(maestro_id).habilitado(habilitado). \
            usuario_id(usuario_id).construir()
        modelo = ConstructorDetalle.id(detalle_id).construir()
        repositorio_detalle.buscar_por_id = MagicMock(return_value=modelo)
        repositorio_detalle.guardar = MagicMock(return_value=detalle_id)

        with self.assertNotRaises(Exception):
            servicio_actualizar_detalle.ejecutar(detalle)

        self.assertEqual(modelo.id, detalle_id)
        self.assertEqual(modelo.valor, valor)
        self.assertEqual(modelo.maestro_id, maestro_id)
        self.assertEqual(modelo.habilitado, habilitado)
        self.assertEqual(modelo.usuario_id, usuario_id)

