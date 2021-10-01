from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from app.comun.modelo.maestro import Maestro


class EsquemaMaestro(SQLAlchemySchema):
    class Meta:
        model = Maestro
        load_intance = True

    id = auto_field()
    nombre = auto_field()
    descripcion = auto_field()
    editable = auto_field()
    habilitado = auto_field()
