#! /usr/bin/env python

import psycopg2
import numpy as np
from datetime import datetime, timedelta

# generate 10 minutes of data, release a new version at 5 minutes
TIME = 10 * 60
RELEASE_AT = 3 * 60

OLD_VERSION = "1.0.7"
NEW_VERSION = "1.0.8"

NUM_APPS = 100

P_EMIT = 0.3
P_SWITCH = 0.1
P_OLD_200 = 0.9
P_NEW_200 = 0.4

if __name__ == '__main__':
  conn = psycopg2.connect(user='postgres', password='postgres', host='127.0.0.1', port='5432', database='postgres')
  cursor = conn.cursor()
  
  insert_query = """INSERT INTO http(status_code, app_version, timestamp) VALUES (%s, %s, %s)"""
  versions = [OLD_VERSION] * NUM_APPS

  for t in range(TIME):
    if t % 30 == 0:
      print('{}/{}'.format(t+1, TIME))

    emit_probs = np.random.uniform(low=0., high=1., size=NUM_APPS)
    status_probs = np.random.uniform(low=0., high=1., size=NUM_APPS)

    if t == RELEASE_AT:
      switch_probs = np.random.uniform(low=0., high=1., size=NUM_APPS)

    for app in range(NUM_APPS):
      if t % 30 == 0 and versions[app] == OLD_VERSION and t >= RELEASE_AT and status_probs[app] <  P_SWITCH:
        versions[app] = NEW_VERSION

      if emit_probs[app] <= P_EMIT:
        timestamp = datetime.now() + timedelta(seconds=t*10)
        status_code = 200
        if versions[app] == OLD_VERSION and status_probs[app] > P_OLD_200:
          status_code = 500
        elif versions[app] == NEW_VERSION and status_probs[app] > P_NEW_200:
          status_code = 500

        cursor.execute(insert_query, (status_code, versions[app], timestamp))
        conn.commit()
  
  conn.close()
