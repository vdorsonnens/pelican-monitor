#! /usr/bin/env python

import psycopg2
import numpy as np
from datetime import datetime, timedelta

# generate 20 hours of data, release a new version at 7 and 14
TIME = 20 * 60
RELEASE_AT = 5 * 60
NEW_RELEASE_AT = 10 * 60

OLD_VERSION = "4.2.0"
NEW_VERSION = "4.2.1"
NEW_NEW_VERSION = "4.2.2"

NUM_APPS = 100

P_EMIT = 0.5
P_SWITCH = 0.05
P_OLD_200 = 0.95
P_NEW_200 = 0.95
P_NEW_NEW_200 = 0.4

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

    if t >= RELEASE_AT:
      switch_probs = np.random.uniform(low=0., high=1., size=NUM_APPS)

    for app in range(NUM_APPS):
      if t % 30 == 0 and t >= RELEASE_AT and switch_probs[app] <  P_SWITCH:
        if t >= NEW_RELEASE_AT:
          versions[app] = NEW_NEW_VERSION
        else:
          versions[app] = NEW_VERSION

      if emit_probs[app] <= P_EMIT:
        timestamp = datetime.now() - timedelta(minutes=TIME) + timedelta(minutes=t)
        status_code = 200
        if versions[app] == OLD_VERSION and status_probs[app] > P_OLD_200:
          status_code = 500
        elif versions[app] == NEW_VERSION and status_probs[app] > P_NEW_200:
          status_code = 500
        elif versions[app] == NEW_NEW_VERSION and status_probs[app] > P_NEW_NEW_200:
          status_code = 500

        cursor.execute(insert_query, (status_code, versions[app], timestamp))
        conn.commit()
  
  conn.close()
