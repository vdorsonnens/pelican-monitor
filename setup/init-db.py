import psycopg2
import os

URL = os.getenv('PG_HOST', 'localhost') 
PORT = '5432'
DBNAME = 'postgres'
DBUSER = 'postgres'
DBPASSWORD = 'postgres'

if __name__ == '__main__':
  # connect to the postgresql docker container
  conn = psycopg2.connect(user=DBUSER, host=URL, password=DBPASSWORD, port=PORT, database=DBNAME)
  cursor = conn.cursor()

  create_table_query = """CREATE TABLE http(id SERIAL PRIMARY KEY, status_code TEXT, app_version TEXT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
  cursor.execute(create_table_query)
  conn.commit()

  conn.close()
