from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from app.comun.modelo.detalle import Detalle


class EsquemaDetalle(SQLAlchemySchema):
    class Meta:
        model = Detalle
        load_intance = True

    id = auto_field()
    valor = auto_field()
    maestro_id = auto_field()
    habilitado = auto_field()
