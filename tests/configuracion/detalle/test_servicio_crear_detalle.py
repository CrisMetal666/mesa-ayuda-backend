from unittest import TestCase
from unittest.mock import MagicMock

from app.comun.excepciones import ExcepcionValorObligatorio, ExcepcionCampoInvalido
from app.comun.modelo.detalle import Detalle
from app.configuracion.detalle.repositorio.repositorio_detalle import RepositorioDetalle
from app.configuracion.detalle.servicio.servicio_crear_detalle import ServicioCrearDetalle
from tests.comun.constructor.constructor_detalle import ConstructorDetalle

repositorio_detalle = RepositorioDetalle()
servicio_crear_detalle = ServicioCrearDetalle(repositorio_detalle)


class TestServicioCrearDetalle(TestCase):

    def test_detalle_con_id(self):
        detalle = ConstructorDetalle.id(1).construir()

        with self.assertRaises(ExcepcionCampoInvalido) as cm:
            servicio_crear_detalle.ejecutar(detalle)

        self.assertEqual(servicio_crear_detalle.MENSAJE_DETALLE_NO_PUEDE_TENER_ID, str(cm.exception))

    def test_detalle_con_valores_faltantes(self):
        with self.assertRaises(ExcepcionValorObligatorio) as cm:
            ConstructorDetalle.habilitado(None).construir()

        self.assertEqual(Detalle.MENSAJE_HABILITADO_OBLIGATORIO, str(cm.exception))

    def test_datos_correctos(self):
        detalle_id = 1
        detalle = ConstructorDetalle.id(None).construir()
        repositorio_detalle.guardar = MagicMock(return_value=detalle_id)

        resultado = servicio_crear_detalle.ejecutar(detalle)

        self.assertEqual(resultado, detalle_id)
