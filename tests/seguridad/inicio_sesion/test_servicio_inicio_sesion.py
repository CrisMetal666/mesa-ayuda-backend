from unittest import TestCase
from unittest.mock import MagicMock

from flask_jwt_extended import create_access_token

from app.comun.excepciones import ExcepcionCredencialesIncorrectas, ExcepcionSinAutorizacion
from app.seguridad.inicio_sesion.dao.dao_inicio_sesion import DaoInicioSesion
from app.seguridad.inicio_sesion.servicio.servicio_inicio_sesion import ServicioInicioSesion
from tests.comun.constructor.constructor_role import ConstructorRole
from tests.comun.constructor.contructor_usuario import ConstructorUsuario

dao_inicio_sesion = DaoInicioSesion()
servicio_inicio_sesion = ServicioInicioSesion(dao_inicio_sesion)


class TestServicioInicioSesion(TestCase):

    def test_ejecutar_usuario_no_encontrado(self):
        dao_inicio_sesion.buscar_usuario_por_identificacion = MagicMock(return_value=None)

        with self.assertRaises(ExcepcionCredencialesIncorrectas) as cm:
            servicio_inicio_sesion.ejecutar('111111', '2222222')

        self.assertEqual(servicio_inicio_sesion.MENSAJE_USUARIO_NO_ENCONTRADO, str(cm.exception))

    def test_ejecutar_clave_incorrecta(self):
        clave = 'pbkdf2:sha256:260000$2YsbCNh0VZF0G6Wq$442529c51ba2bf1f7bd78bea1e30b332820fac600db89b0f77597d6fd9e21a2a'
        usuario = ConstructorUsuario.clave(clave).construir()
        dao_inicio_sesion.buscar_usuario_por_identificacion = MagicMock(return_value=usuario)

        with self.assertRaises(ExcepcionCredencialesIncorrectas) as cm:
            servicio_inicio_sesion.ejecutar('11111', '22222')

        self.assertEqual(servicio_inicio_sesion.MENSAJE_CLAVE_INVALIDA, str(cm.exception))

    def test_ejecutar_usuario_inhabilitado(self):
        clave = 'pbkdf2:sha256:260000$2YsbCNh0VZF0G6Wq$442529c51ba2bf1f7bd78bea1e30b332820fac600db89b0f77597d6fd9e21a2a'
        usuario = ConstructorUsuario.clave(clave).habilitado(False).construir()
        dao_inicio_sesion.buscar_usuario_por_identificacion = MagicMock(return_value=usuario)
        dao_inicio_sesion.buscar_role_por_usuario = MagicMock(return_value=[])

        with self.assertRaises(ExcepcionSinAutorizacion) as cm:
            servicio_inicio_sesion.ejecutar('11111', 'cris232322')

        self.assertEqual(servicio_inicio_sesion.MENSAJE_USUARIO_INHABILITADO, str(cm.exception))

    def test_ejecutar_sin_roles_asignados(self):
        clave = 'pbkdf2:sha256:260000$2YsbCNh0VZF0G6Wq$442529c51ba2bf1f7bd78bea1e30b332820fac600db89b0f77597d6fd9e21a2a'
        usuario = ConstructorUsuario.clave(clave).construir()
        dao_inicio_sesion.buscar_usuario_por_identificacion = MagicMock(return_value=usuario)
        dao_inicio_sesion.buscar_role_por_usuario = MagicMock(return_value=[])

        with self.assertRaises(ExcepcionSinAutorizacion) as cm:
            servicio_inicio_sesion.ejecutar('11111', 'cris232322')

        self.assertEqual(servicio_inicio_sesion.MENSAJE_SIN_ROLE_ASIGNADO, str(cm.exception))

    def test_ejecutar_credenciales_correctas(self):
        clave = 'pbkdf2:sha256:260000$2YsbCNh0VZF0G6Wq$442529c51ba2bf1f7bd78bea1e30b332820fac600db89b0f77597d6fd9e21a2a'
        usuario = ConstructorUsuario.clave(clave).construir()
        dao_inicio_sesion.buscar_usuario_por_identificacion = MagicMock(return_value=usuario)
        role = ConstructorRole.nombre('ROLE_ADMIN').construir()
        dao_inicio_sesion.buscar_role_por_usuario = MagicMock(return_value=[role])
        servicio_inicio_sesion._generar_token = MagicMock(return_value='asdfsdf.sdfsdfs.sdfsdf')

        token = servicio_inicio_sesion.ejecutar('11111', 'cris232322')

        self.assertGreater(len(token), 0)
