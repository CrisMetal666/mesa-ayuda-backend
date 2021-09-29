"""
from unittest import TestCase
from unittest.mock import MagicMock

from app.comun.modelo.usuario_prueba import UsuarioPrueba
from app.demo.usuario.repositorio.repositorio_usuario import RepositorioUsuario
from app.demo.usuario.servicio.servicio_crear_usuario import ServicioCrearUsuario

repositorio_usuario = RepositorioUsuario()
servicio_crear_usuario = ServicioCrearUsuario(repositorio_usuario)


class TestServicioCrearUsuario(TestCase):

    def test_probando(self):
        repositorio_usuario.crear = MagicMock(return_value=3)
        id = servicio_crear_usuario.ejecutar(ConstructorUsuarioPrueba.construir())
        self.assertEqual(id, 3)


class ConstructorUsuarioPrueba:
    field_id = 1
    field_nombre = 'Nnombre'
    field_apellido = 'Apellido'
    field_correo = 'Correo'
    field_clave = 'Clave'

    @classmethod
    def id(cls, field_id):
        cls.field_id = field_id
        return cls

    @classmethod
    def nombre(cls, field_nombre):
        cls.field_nombre = field_nombre
        return cls

    @classmethod
    def apellido(cls, field_apellido):
        cls.field_apellido = field_apellido
        return cls

    @classmethod
    def correo(cls, field_correo):
        cls.field_correo = field_correo
        return cls

    @classmethod
    def clave(cls, field_clave):
        cls.field_clave = field_clave
        return cls

    @classmethod
    def construir(cls):
        print(cls.field_id, cls.field_nombre, cls.field_apellido)
        return UsuarioPrueba(cls.field_id, cls.field_nombre, cls.field_apellido, cls.field_correo, cls.field_clave)
"""