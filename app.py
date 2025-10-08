from flask import Flask, render_template, request, redirect
from sqlalchemy import select
from db import get_session
from models import Region

app = Flask(__name__)

@app.route('/')
def portada():
    return render_template("index.html")

@app.route('/aviso_form', methods=['GET', 'POST'])
def aviso_form():
    session = get_session()

    if request.method == 'POST':
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
    return render_template('aviso_list.html')
    
@app.route('/stats')
def stats():
    return render_template('stats.html')


if __name__ == "__main__":
    app.run()

