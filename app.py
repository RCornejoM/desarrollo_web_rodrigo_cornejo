from flask import Flask, render_template
from sqlalchemy import select, desc
from db import get_session

app = Flask(__name__)

@app.route('/')
def portada():
    session = get_session()

    return render_template('index.html')

if __name__ == "__main__":
    app.run()

