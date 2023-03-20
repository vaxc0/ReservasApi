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
            "carrera": self.carrera,
            "password": self.password
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
    min = db.Column(db.Integer, nullable=False)
    max = db.Column(db.Integer, nullable=False)

    def __init__(self, nombre, min, max, id=None):
        self.id = id
        self.nombre = nombre
        self.min = min
        self.max = max

    def to_json(self) -> str:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "min": self.min,
            "max": self.max
        }


class EspacioFisico(db.Model):
    __tablename__ = 'espacios_fisicos'

    id = db.Column(db.Integer, primary_key=True)
    id_regla = db.Column(db.Integer, db.ForeignKey('reglas.id'))
    facultad = db.Column(db.String, nullable=False)
    bloque = db.Column(db.String, nullable=False)
    tipo = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    aforo = db.Column(db.Integer)
    reservable = db.Column(db.Integer)
    reservado = db.Column(db.Integer)
    # tipo = db.relationship("Tipo", backref="tipos",lazy=True)

    def __init__(self, facultad, bloque, tipo, nombre, aforo, reservable, reservado, id=None, id_regla=None):
        self.id = id
        self.id_regla = id_regla
        self.facultad = facultad
        self.bloque = bloque
        self.tipo = tipo
        self.nombre = nombre
        self.aforo = aforo
        self.reservable = reservable
        self.reservado = reservado

    def to_json(self) -> str:
        return {
            "id": self.id,
            "id_regla": self.id_regla,
            "facultad": self.facultad,
            "bloque": self.bloque,
            "tipo": self.tipo,
            "nombre": self.nombre,
            "aforo": self.aforo,
            "reservable": self.reservable,
            "reservado": self.reservado
        }


class Regla(db.Model):
    __tablename__ = 'reglas'

    id = db.Column(db.Integer, primary_key=True)
    horas_uso = db.Column(db.Integer)
    horas_nueva_reserva = db.Column(db.Integer)
    tiempo_espera = db.Column(db.Integer)

    def __init__(self, horas_uso, horas_nueva_Reserva, tiempo_espera, id=None) -> None:
        self.id = id
        self.horas_uso = horas_uso
        self.horas_nueva_reserva = horas_nueva_Reserva
        self.tiempo_espera = tiempo_espera

    def to_json(self) -> str:
        return {
            "id": self.id,
            "horas_uso": self.horas_uso,
            "horas_nueva_reserva": self.horas_nueva_reserva,
            "tiempo_espera": self.tiempo_espera
        }


class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    id_operario = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer, nullable=False)
    id_espacioFisico = db.Column(db.Integer, nullable=False)
    activa = db.Column(db.Integer)
    vencida = db.Column(db.Integer)
    fechaHora_realizada = db.Column(db.DateTime)
    fecha_reservar = db.Column(db.DateTime)
    hora_reservar = db.Column(db.DateTime)
    hora_finalReservar = db.Column(db.DateTime)

    def __init__(self, id_usuario, id_operario, id_espacioFisico, activa, vencida, fechaHora_realizada, fecha_reservar, hora_reservar, hora_finalReservar, id=None):
        self.id = id
        self.id_operario = id_operario
        self.id_usuario = id_usuario
        self.id_espacioFisico = id_espacioFisico
        self.activa = activa
        self.vencida = vencida
        self.fechaHora_realizada = fechaHora_realizada
        self.fecha_reservar = fecha_reservar
        self.hora_reservar = hora_reservar
        self.hora_finalReservar = hora_finalReservar

    def to_json(self) -> str:
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_operario": self.id_operario,
            "id_espacioFisico": self.id_espacioFisico,
            "activa": self.activa,
            "vencida": self.vencida,
            "fechaHora_realizada": self.fechaHora_realizada,
            "fecha_reservar": self.fecha_reservar,
            "hora_reservar": self.hora_reservar,
            "hora_finalReservar": self.hora_finalReservar,
        }
