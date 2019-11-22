#! /usr/bin/python
import os
import json
import requests

GRAFANA_HOST = os.getenv('GRAFANA_HOST', 'localhost')
GRAFANA_URL = 'http://admin:admin@{}:3000/api'.format(GRAFANA_HOST)

DIR = os.path.dirname(__file__)
DASHBOARD_FILE = os.path.join(DIR, 'dashboard2.json')
DATASOURCE_FILE = os.path.join(DIR, 'datasource.json')

if __name__ == '__main__':
  # read and parse the dashboard file
  with open(DASHBOARD_FILE, 'r') as f:
    data = f.read()

  dashboard = json.loads(data)
  
  # read and parse the data source file
  with open(DATASOURCE_FILE, 'r') as f:
    data = f.read()

  datasource = json.loads(data)
  
  # create the data source on the container
  resp = requests.post(GRAFANA_URL + '/datasources', json=datasource)
  resp = requests.post(GRAFANA_URL + '/dashboards/db', json=dashboard)
