#! /usr/bin/env bash

pip install -r requirements.txt
if [ $? -ne 0 ]; then
  echo "Failed to install the requirements" >&2
  exit 1
fi

python init-db.py
python init-grafana.py
