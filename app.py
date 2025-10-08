from flask import Flask, render_template, redirect, request
from sqlalchemy import select, desc
from db import get_session

app = Flask(__name__)

@app.route('/')
def portada():
    session = get_session()
    return render_template('index.html')

@app.route('/aviso_form', methods=['GET', 'POST'])
def aviso_form():
    if request.method == 'POST':
        return redirect('/portada')
    return render_template('aviso_form.html')

@app.route('/aviso_list')
def aviso_list():
    return render_template('aviso_list.html')
    
@app.route('/stats')
def stats():
    return render_template('stats.html')


if __name__ == "__main__":
    app.run()

