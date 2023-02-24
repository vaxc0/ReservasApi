from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    documento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40))
    apellido = db.Column(db.String(40))
    edad = db.Column(db.Integer())
    carrera = db.Column(db.String(40))
    password = db.Column(db.String())

    def __init__(self, documento, id_rol, password, nombre=None, apellido=None, edad=None, carrera=None) -> None:
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carrera = carrera
        self.id_rol = id_rol
        self.password = password

    def to_json(self) -> str:
        return {
            "id_rol": self.id_rol,
            "documento": self.documento,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "carrera": self.carrera
        }


class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(30))

    def __init__(self, rol, id=None) -> None:
        self.id = id
        self.rol = rol

    def to_json(self) -> str:
        return {
            "id": self.id,
            "rol": self.rol
        }


class Facultad(db.Model):
    __tablename__ = 'facultades'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, id=None) -> None:
        self.id = id
        self.nombre = nombre

    def to_json(self) -> str:
        return {
            "id": self.id,
            "nombre": self.nombre
        }


class Bloque(db.Model):
    __tablename__ = 'bloques'

    id = db.Column(db.Integer, primary_key=True)
    bloque = db.Column(db.CHAR(1), nullable=False)

    def __init__(self, bloque, id=None):
        self.id = id
        self.bloque = bloque

    def to_json(self) -> str:
        return {
            "id": self.id,
            "bloque": self.bloque
        }


class Tipo(db.Model):
    __tablename__ = 'tipos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, id=None):
        self.id = id
        self.nombre = nombre

    def to_json(self) -> str:
        return {
            "id": self.id,
            "nombre": self.nombre
        }


class EspacioFisico(db.Model):
    __tablename__ = 'espacios_fisicos'

    id = db.Column(db.Integer, primary_key=True)
    id_facultad = db.Column(db.Integer, db.ForeignKey(
        'facultades.id'), nullable=False)
    id_bloque = db.Column(db.Integer, db.ForeignKey(
        'bloques.id'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipos.id'), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    aforo = db.Column(db.Integer, nullable=False)
    horas_uso = db.Column(db.Time, nullable=False)
    horas_nueva_reserva = db.Column(db.Time, nullable=False)
    tiempo_espera = db.Column(db.Time, nullable=False)
    reservable = db.Column(db.Boolean)
    reservado = db.Column(db.Boolean)
    # tipo = db.relationship("Tipo", backref="tipos",lazy=True)

    def __init__(self, id_facultad, id_bloque, id_tipo, nombre, aforo, horas_uso, horas_nueva_reserva,
                 tiempo_espera, reservable=True, reservado=False, id=None):
        self.id = id
        self.id_facultad = id_facultad
        self.id_bloque = id_bloque
        self.id_tipo = id_tipo
        self.nombre = nombre
        self.aforo = aforo
        self.horas_uso = horas_uso
        self.horas_nueva_reserva = horas_nueva_reserva
        self.tiempo_espera = tiempo_espera
        self.reservable = reservable
        self.reservado = reservado

    def to_json(self) -> str:
        return {
            "id": self.id,
            "id_facultad": self.id_facultad,
            "id_bloque": self.id_bloque,
            "id_tipo": self.id_tipo,
            "nombre": self.nombre,
            "aforo": self.aforo,
            "horas_uso": self.horas_uso,
            "horas_nueva_reserva": self.horas_nueva_reserva,
            "tiempo_espera": self.tiempo_espera,
            "reservable": self.reservable,
            "reservado": self.reservado
        }
