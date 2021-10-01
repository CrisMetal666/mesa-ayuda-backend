from app.comun.modelo.detalle import Detalle


class ConstructorDetalle:
    campo_id = 1
    campo_valor = 'Valor1'
    campo_maestro_id = 1
    campo_habilitado = True
    campo_usuario_id = 1

    @classmethod
    def id(cls, id):
        cls.campo_id = id
        return cls

    @classmethod
    def valor(cls, valor):
        cls.campo_valor = valor
        return cls

    @classmethod
    def maestro_id(cls, maestro_id):
        cls.campo_maestro_id = maestro_id
        return cls

    @classmethod
    def habilitado(cls, habilitado):
        cls.campo_habilitado = habilitado
        return cls

    @classmethod
    def construir(cls):
        return Detalle(
            id=cls.campo_id,
            valor=cls.campo_valor,
            maestro_id=cls.campo_maestro_id,
            habilitado=cls.campo_habilitado,
            usuario_id=cls.campo_usuario_id
        )
