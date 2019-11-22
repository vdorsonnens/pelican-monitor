#! /usr/bin/bash

pip install -r requirements.txt

python init-db.py
python init-grafana.py
