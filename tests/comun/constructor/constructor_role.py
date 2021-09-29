from app.comun.modelo.role import Role


class ConstructorRole:
    campo_id = 1
    campo_nombre = ''
    campo_habilitado = True
    campo_usuario_id = 1

    @classmethod
    def id(cls, id):
        cls.campo_id = id
        return cls

    @classmethod
    def nombre(cls, nombre):
        cls.campo_nombre = nombre
        return cls

    @classmethod
    def habilitado(cls, habilitado):
        cls.campo_habilitado = habilitado
        return cls

    @classmethod
    def usuario_id(cls, usuario_id):
        cls.campo_usuario_id = usuario_id
        return cls

    @classmethod
    def construir(cls):
        return Role(
            id=cls.campo_id,
            nombre=cls.campo_nombre,
            habilitado=cls.campo_habilitado,
            usuario_id=cls.campo_usuario_id
        )
