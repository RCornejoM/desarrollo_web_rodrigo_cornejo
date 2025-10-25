#!/bin/bash
python3 -m venv venv
source venv/bin/activate || source venv/Scripts/activate
pip install -r requirements.txt
sudo mysql -u cc5002 -p -e "CREATE DATABASE IF NOT EXISTS tarea2;"
sudo mysql -u cc5002 -p tarea2 < region-comuna.sql
sudo mysql -u cc5002 -p tarea2 < tarea2.sql
sudo mysql -u cc5002 -p tarea2 < tabla-comentarios.sql
python3 create_tables.py
flask --app app.py run

