from flask import Flask, render_template, request, redirect, flash
from sqlalchemy import select
from db import get_session
from models import Region, AvisoAdopcion, Foto, ContactarPor
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def portada():
    session = get_session()
    avisos = session.scalars(select(AvisoAdopcion)).all()
    return render_template("index.html", avisos=avisos)
    
@app.route('/aviso_form', methods=['GET', 'POST'])
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
            cp = ContactarPor(
                nombre=contactar_por,
                identificador=identificador,
                actividad_id=nuevo_aviso.id
            )
            session.add(cp)

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
    avisos = session.scalars(select(AvisoAdopcion)).all()
    return render_template('aviso_list.html', avisos=avisos)
    
@app.route('/aviso/<int:aviso_id>')
def detalle_aviso(aviso_id):
    session = get_session()
    aviso = session.get(AvisoAdopcion, aviso_id)
    if not aviso:
        abort(404)
    return render_template("aviso_card.html", aviso=aviso)
   
@app.route('/stats')
def stats():
    return render_template('stats.html')


if __name__ == "__main__":
    app.run()

