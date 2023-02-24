from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from utils.PageFormat import toJson
from models.models import *

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postv4x@localhost:5432/udes_api"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello():
    return "<h1>APi ORM</h1>"


@app.route('/api/roles/', methods=['GET', 'POST'])
def getAll_add_roles():
    if request.method == 'GET':
        try:
            paginated = request.args.get("paginated", False, type=bool)

            if paginated:
                page = request.args.get("page", 1, type=int)
                per_page = request.args.get("per-page", 10, type=int)
                page_rol = Rol.query.paginate(
                per_page=per_page, page=page, error_out=True)
                results = []

                for rol in page_rol.items:
                    results.append(rol.to_json())

                return jsonify(toJson.page_format(results, page_rol))
            else:
                roles = Rol.query.all()
                results = []

                for rol in roles:
                    results.append(rol.to_json())

                return jsonify(results)
        except Exception as e:
            print(e)
            return jsonify({'message':  str(e)})

    elif request.method == 'POST':
        try:
            if not request.is_json:
                return jsonify({"error": "La carga útil de la solicitud no está en formato JSON"})
            else:
                data = request.get_json()
                new_rol = Rol(rol=data['rol'])
                db.session.add(new_rol)
                db.session.commit()
                return jsonify({"message": "Creado Correctamente", "added": new_rol.to_json()})

        except Exception as e:
            return jsonify({'message':  str(e)})


@app.route('/api/roles/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_upd_del_rol(id):
    rol = Rol.query.get(id)
    if not rol:
        return jsonify({'message': "Rol no Encontrado"})
    else:
        if request.method == 'GET':
            return jsonify(rol.to_json())

        elif request.method == 'PUT':
            new_data = request.get_json()
            rol.rol = new_data['rol']
            db.session.add(rol)
            db.session.commit()
            return jsonify({"message": "Actualizado Correctamente", "modiffied": rol.to_json()})

        elif request.method == 'DELETE':
            db.session.delete(rol)
            db.session.commit()
            return jsonify({'message': "Eliminado Correctamente"})


@app.route('/api/usuarios/', methods=['GET', 'POST'])
def getAll_add_usuarios():
    if request.method == 'GET':
        paginated = request.args.get("paginated", False, type=bool)

        if paginated:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per-page", 10, type=int)
            page_usuario = Usuario.query.paginate(
                per_page=per_page, page=page, error_out=True)
            results = []

            for usuario in page_usuario.items:
                results.append(usuario.to_json())

            return jsonify(toJson.page_format(results, page_usuario))
        else:
            usuarios = Usuario.query.all()
            results = []

            for usuario in usuarios:
                results.append(usuario.to_json())

            return jsonify(results)

    elif request.method == 'POST':
        try:
            if not request.is_json:
                return jsonify({"error": "La carga útil de la solicitud no está en formato JSON"})
            else:
                data = request.get_json()
                new_usuario = Usuario(
                    id_rol=data['id_rol'],
                    documento=data['documento'],
                    password=data['password']
                )
                db.session.add(new_usuario)
                db.session.commit()
                return jsonify({"message": "Creado Correctamente", "added": new_usuario.to_json()})

        except Exception as e:
            return jsonify({'message':  str(e)})


@app.route('/api/usuarios/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_upd_del_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'message': "Usuario no Encontrado"})
    else:
        if request.method == 'GET':
            return jsonify(usuario.to_json())

        elif request.method == 'PUT':
            new_data = request.get_json()
            usuario.documento = new_data['documento'],
            usuario.nombre = new_data['nombre'],
            usuario.apellido = new_data['apellido'],
            usuario.edad = new_data['edad'],
            usuario.carrera = new_data['carrera'],
            usuario.password = new_data['password']
            db.session.add(usuario)
            db.session.commit()
            return jsonify({"message": "Actualizado Correctamente", "modiffied": usuario.to_json()})

        elif request.method == 'DELETE':
            db.session.delete(usuario)
            db.session.commit()
            return jsonify({'message': "Eliminado Correctamente"})


@app.route('/api/bloques/', methods=['GET', 'POST'])
def getAll_add_bloques():
    if request.method == 'GET':
        paginated = request.args.get("paginated", False, type=bool)

        if paginated:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per-page", 10, type=int)
            page_bloque = Bloque.query.paginate(
                per_page=per_page, page=page, error_out=True)
            results = []

            for bloque in page_bloque.items:
                results.append(bloque.to_json())

            return jsonify(toJson.page_format(results, page_bloque))
        else:
            bloques = Bloque.query.all()
            results = []

            for bloque in bloques:
                results.append(bloque.to_json())

            return jsonify(results)

    elif request.method == 'POST':
        try:
            if not request.is_json:
                return jsonify({"error": "La carga útil de la solicitud no está en formato JSON"})
            else:
                data = request.get_json()
                new_bloque = Bloque(bloque=data['bloque'])
                db.session.add(new_bloque)
                db.session.commit()
                return jsonify({"message": "Creado Correctamente", "added": new_bloque.to_json()})

        except Exception as e:
            return jsonify({'message':  str(e)})


@app.route('/api/bloques/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_upd_del_bloque(id):
    bloque = Bloque.query.get(id)
    if not bloque:
        return jsonify({'message': "Bloque no Encontrado"})
    else:
        if request.method == 'GET':
            return jsonify(bloque.to_json())

        elif request.method == 'PUT':
            new_data = request.get_json()
            bloque.bloque = new_data['bloque']
            db.session.add(bloque)
            db.session.commit()
            return jsonify({"message": "Actualizado Correctamente", "modiffied": bloque.to_json()})

        elif request.method == 'DELETE':
            db.session.delete(bloque)
            db.session.commit()
            return jsonify({'message': "Eliminado Correctamente"})


@app.route('/api/tipos/', methods=['GET', 'POST'])
def getAll_add_tipos():
    if request.method == 'GET':
        paginated = request.args.get("paginated", False, type=bool)

        if paginated:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per-page", 10, type=int)
            page_tipo = Tipo.query.paginate(
                per_page=per_page, page=page, error_out=True)
            results = []

            for tipo in page_tipo.items:
                results.append(tipo.to_json())

            return jsonify(toJson.page_format(results, page_tipo))
        else:
            tipos = Tipo.query.all()
            results = []

            for tipo in tipos:
                results.append(tipo.to_json())

            return jsonify(results)

    elif request.method == 'POST':
        try:
            if not request.is_json:
                return jsonify({"error": "La carga útil de la solicitud no está en formato JSON"})
            else:
                data = request.get_json()
                new_tipo = Tipo(nombre=data['nombre'])
                db.session.add(new_tipo)
                db.session.commit()
                return jsonify({"message": "Creado Correctamente", "added": new_tipo.to_json()})

        except Exception as e:
            return jsonify({'message':  str(e)})


@app.route('/api/tipos/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_upd_del_tipo(id):
    tipo = Tipo.query.get(id)
    if not tipo:
        return jsonify({'message': "Tipo no Encontrado"})
    else:
        if request.method == 'GET':
            return jsonify(tipo.to_json())

        elif request.method == 'PUT':
            new_data = request.get_json()
            tipo.nombre = new_data['nombre']
            db.session.add(tipo)
            db.session.commit()
            return jsonify({"message": "Actualizado Correctamente", "modiffied": tipo.to_json()})

        elif request.method == 'DELETE':
            db.session.delete(tipo)
            db.session.commit()
            return jsonify({'message': "Eliminado Correctamente"})


@app.route('/api/facultades/', methods=['GET', 'POST'])
def getAll_add_facultades():
    if request.method == 'GET':
        paginated = request.args.get("paginated", False, type=bool)

        if paginated:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per-page", 10, type=int)
            page_facultad = Facultad.query.paginate(
                per_page=per_page, page=page, error_out=True)
            results = []

            for facultad in page_facultad.items:
                results.append(facultad.to_json())

            return jsonify(toJson.page_format(results, page_facultad))
        else:
            facultades = Facultad.query.all()
            results = []

            for facultad in facultades:
                results.append(facultad.to_json())

            return jsonify(results)

    elif request.method == 'POST':
        try:
            if not request.is_json:
                return jsonify({"error": "La carga útil de la solicitud no está en formato JSON"})
            else:
                data = request.get_json()
                new_facultad = Facultad(nombre=data['nombre'])
                db.session.add(new_facultad)
                db.session.commit()
                return jsonify({"message": "Creado Correctamente", "added": new_facultad.to_json()})

        except Exception as e:
            return jsonify({'message':  str(e)})


@app.route('/api/facultades/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_upd_del_facultad(id):
    facultad = Facultad.query.get(id)
    if not facultad:
        return jsonify({'message': "Facultad no Encontrada"})
    else:
        if request.method == 'GET':
            return jsonify(facultad.to_json())

        elif request.method == 'PUT':
            new_data = request.get_json()
            facultad.nombre = new_data['nombre']
            db.session.add(facultad)
            db.session.commit()
            return jsonify({"message": "Actualizado Correctamente", "modiffied": facultad.to_json()})

        elif request.method == 'DELETE':
            db.session.delete(facultad)
            db.session.commit()
            return jsonify({'message': "Eliminado Correctamente"})


@app.route('/api/espaciosFisicos/', methods=['GET', 'POST'])
def getAll_add_espaciosFisicos():
    if request.method == 'GET':
        paginated = request.args.get("paginated", False, type=bool)

        if paginated:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per-page", 10, type=int)
            page_espacioF = EspacioFisico.query.paginate(
                per_page=per_page, page=page, error_out=True)
            results = []

            for espacioF in page_espacioF.items:
                results.append(espacioF.to_json())

            return jsonify(toJson.page_format(results, page_espacioF))
        else:
            espaciosFisicos = EspacioFisico.query.all()
            results = []

            for espacioF in espaciosFisicos:
                results.append(espacioF.to_json())

            return jsonify(results)

    elif request.method == 'POST':
        try:
            if not request.is_json:
                return jsonify({"error": "La carga útil de la solicitud no está en formato JSON"})
            else:
                data = request.get_json()
                new_espacioF = EspacioFisico(
                    id_facultad=data['id_facultad'],
                    id_bloque=data['id_bloque'],
                    id_tipo=data['id_bloque'],
                    nombre=data['nombre'],
                    aforo=data['aforo'],
                    horas_uso=data['horas_uso'],
                    horas_nueva_reserva=data['horas_nueva_reserva'],
                    tiempo_espera=data['tiempo_espera'],
                    reservable=data['reservable'],
                    reservado=data['reservado']
                )
                db.session.add(new_espacioF)
                db.session.commit()
                return jsonify({"message": "Creado Correctamente", "added": new_espacioF.to_json()})

        except Exception as e:
            return jsonify({'message':  str(e)})


@app.route('/api/espaciosFisicos/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_upd_del_espacioFisico(id):
    espacioF = EspacioFisico.query.get(id)
    if not espacioF:
        return jsonify({'message': "Espacio Fisico no Encontrado"})
    else:
        if request.method == 'GET':
            return jsonify(espacioF.to_json())

        elif request.method == 'PUT':
            new_data = request.get_json()
            espacioF.id_facultad = new_data['id_facultad'],
            espacioF.id_bloque = new_data['id_bloque'],
            espacioF.id_tipo = new_data['id_bloque'],
            espacioF.nombre = new_data['nombre'],
            espacioF.aforo = new_data['aforo'],
            espacioF.horas_uso = new_data['horas_uso'],
            espacioF.horas_nueva_reserva = new_data['horas_nueva_reserva'],
            espacioF.tiempo_espera = new_data['tiempo_espera'],
            espacioF.reservable = new_data['reservable'],
            espacioF.reservado = new_data['reservado']
            db.session.add(espacioF)
            db.session.commit()
            return jsonify({"message": "Actualizado Correctamente", "modiffied": espacioF.to_json()})

        elif request.method == 'DELETE':
            db.session.delete(espacioF)
            db.session.commit()
            return jsonify({'message': "Eliminado Correctamente"})


def page_not_found(eror):
    return "<h1>La pagina no se ha Encontrado</h1>", 404


if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)