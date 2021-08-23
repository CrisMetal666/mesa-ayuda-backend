from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from app.comun.modelo.usuario_prueba import UsuarioPrueba


class EsquemaUsuarioPrueba(SQLAlchemySchema):
    class Meta:
        model = UsuarioPrueba
        load_instace = True

    id = auto_field()
    nombre = auto_field()
    apellido = auto_field()
    correo = auto_field()

