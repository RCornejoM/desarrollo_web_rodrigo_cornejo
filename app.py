from flask import Flask, render_template, request, redirect, flash, make_response
from sqlalchemy import select
from db import get_session
from models import Region, AvisoAdopcion, Foto, ContactarPor, Comentario
from datetime import datetime
from math import ceil

app = Flask(__name__)

@app.route('/')
def portada():
    session = get_session()
    avisos = session.scalars(select(AvisoAdopcion)).all()
    return render_template("index.html", avisos=avisos)
    
@app.route('/aviso_form', methods=['GET', 'POST'])
def aviso_form():
    session = get_session()

    if request.method == 'POST':
   
        comuna_id = request.form.get("comuna")
        if not comuna_id:
            return "Debe seleccionar una comuna", 400
        try:
            comuna_id = int(comuna_id)
        except ValueError:
            return "Comuna inválida", 400

        sector = request.form.get("sector", "").strip()
        if not sector:
            return "Debe ingresar el sector", 400

        nombre = request.form.get("nombre", "").strip()
        if not nombre:
            return "Debe ingresar su nombre", 400

        email = request.form.get("email", "").strip()
        if not email:
            return "Debe ingresar un email", 400

        celular = request.form.get("celular", "").strip()
        if not celular:
            return "Debe ingresar un celular", 400

        tipo = request.form.get("tipo")
        if tipo not in ("gato", "perro"):
            return "Debe seleccionar el tipo de mascota", 400

        cantidad = request.form.get("cantidad")
        try:
            cantidad = int(cantidad)
            if cantidad < 1:
                raise ValueError
        except (ValueError, TypeError):
            return "Cantidad inválida", 400

        edad = request.form.get("edad")
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError
        except (ValueError, TypeError):
            return "Edad inválida", 400

        unidad_medida = request.form.get("unidad_medida")
        if unidad_medida not in ("a", "m"):
            return "Debe seleccionar unidad de medida", 400

        fecha_entrega_str = request.form.get("fecha_entrega")
        fecha_entrega = None
        if fecha_entrega_str:
            try:
                fecha_entrega = datetime.fromisoformat(fecha_entrega_str)
            except ValueError:
                return "Fecha de entrega inválida", 400

        descripcion = request.form.get("descripcion", "").strip()
        if not descripcion:
            return "Debe agregar una descripción", 400

        nuevo_aviso = AvisoAdopcion(
            comuna_id=comuna_id,
            sector=sector,
            nombre=nombre,
            email=email,
            celular=celular,
            tipo=tipo,
            cantidad=cantidad,
            edad=edad,
            unidad_medida=unidad_medida,
            fecha_entrega=fecha_entrega,
            descripcion=descripcion
        )
        session.add(nuevo_aviso)
        session.commit()  

        contactar_por = request.form.get("contactar_por")
        identificador = request.form.get("identificador", "").strip()
        if contactar_por and identificador:
            cont_por = ContactarPor(
                nombre=contactar_por,
                identificador=identificador,
                actividad_id=nuevo_aviso.id
            )
            session.add(cont_por)

        session.commit()
        return redirect('/')

    regiones = session.scalars(select(Region)).all()
    regiones_data = [
        {
            "id": r.id,
            "nombre": r.nombre,
            "comunas": [{"id": c.id, "nombre": c.nombre} for c in r.comunas]
        }
        for r in regiones
    ]
    
    return render_template("aviso_form.html", regiones_data=regiones_data)

@app.route('/aviso_list')
def aviso_list():
    session = get_session()
    page = request.args.get("page", 1, type=int)
    per_page = 5

    all_avisos = session.scalars(select(AvisoAdopcion)).all()
    total = ceil(len(all_avisos) / per_page)
    
    start = (page-1)*per_page
    end = start + per_page
    avisos = all_avisos[start:end]

    return render_template('aviso_list.html', avisos=avisos, page=page, total_pages=total)

    
@app.route('/aviso/<int:aviso_id>')
def detalle_aviso(aviso_id):
    session = get_session()
    aviso = session.get(AvisoAdopcion, aviso_id)
    return render_template("aviso_card.html", aviso=aviso)
   
@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/agregar_comentario', methods=['POST'])
def agregar_comentario():
    session = get_session()
    
    aviso_id = request.form.get("aviso_id")
    nombre = request.form.get("nombre", "").strip()
    texto = request.form.get("texto", "").strip()

    if not nombre or len(nombre) < 3 or len(nombre) > 80:
        return "Nombre inválido (3-80 caracteres)", 400
    if not texto or len(texto) < 5:
        return "Comentario inválido (mínimo 5 caracteres)", 400

    nuevo_comentario = Comentario(
        aviso_id=int(aviso_id),
        nombre=nombre,
        texto=texto,
        fecha=datetime.now()
    )
    session.add(nuevo_comentario)
    session.commit()
    
    return f"<strong>{nombre}</strong> (Ahora): {texto}"


@app.route('/datos_line')
def datos_line():
    session = get_session()
    avisos = session.scalars(select(AvisoAdopcion)).all()

    dias = ['Lun','Mar','Mié','Jue','Vie','Sáb','Dom']
    cantidades = [0,0,0,0,0,0,0]
    for aviso in avisos:
        dia = aviso.fecha_ingreso.weekday()  # lunes=0
        cantidades[dia] += 1

    texto = "["
    for c in cantidades:
        texto += str(c)+","
    texto = texto[:-1]
    texto += "]"

    resp = make_response(texto)
    resp.headers["Content-type"] = "application/json;charset=UTF-8"
    resp.headers["Cache-Control"] = "no-cache"
    return resp

@app.route('/datos_pie')
def datos_pie():
    session = get_session()
    avisos = session.scalars(select(AvisoAdopcion)).all()

    gatos = 0
    perros = 0
    for aviso in avisos:
        if aviso.tipo == 'gato':
            gatos += 1
        else:
            perros += 1

    texto = '[{"name":"Gatos","y":'+str(gatos)+'},{"name":"Perros","y":'+str(perros)+'}]'
    resp = make_response(texto)
    resp.headers["Content-type"] = "application/json;charset=UTF-8"
    resp.headers["Cache-Control"] = "no-cache"
    return resp

@app.route('/datos_bars')
def datos_bars():
    session = get_session()
    avisos = session.scalars(select(AvisoAdopcion)).all()

    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    gatos = [0]*12
    perros = [0]*12
    for aviso in avisos:
        mes = aviso.fecha_ingreso.month-1
        if aviso.tipo == 'gato':
            gatos[mes] += 1
        else:
            perros[mes] += 1

    texto = '{"gatos":['+','.join(map(str,gatos))+'], "perros":['+','.join(map(str,perros))+']}'
    resp = make_response(texto)
    resp.headers["Content-type"] = "application/json;charset=UTF-8"
    resp.headers["Cache-Control"] = "no-cache"
    return resp

if __name__ == "__main__":
    app.run()

