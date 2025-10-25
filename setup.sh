#!/bin/bash
python3 -m venv venv
source venv/bin/activate || source venv/Scripts/activate
pip install -r requirements.txt
python3 create_tables.py
flask --app app.py run

