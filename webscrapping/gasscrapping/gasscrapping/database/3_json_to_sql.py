import psycopg2
import json

host = 'localhost'
port = 5432
user = 'postgres'
password = '1511'
database = 'rasa_bots'

conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)


cursor = conn.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS Gas_stations (
    id serial PRIMARY KEY,
    station_name text,
    price_100 numeric,
    price_92 numeric,
    price_95 numeric,
    price_spbt numeric,
    price_dt numeric,
    price_metan numeric,
    price_premium_92 numeric,
    price_premium_95 numeric,
    price_premium_dt numeric,
    address text
);
"""
cursor.execute(create_table_query)

conn.commit()

with open('output.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

for item in data:
    station_name = item.get('station-name')
    price_100 = item.get('price_100')
    price_92 = item.get('price_92')
    price_95 = item.get('price_95')
    price_spbt = item.get('price_spbt')
    price_dt = item.get('price_dt')
    price_metan = item.get('price_metan')
    price_premium_92 = item.get('price_premium_92')
    price_premium_95 = item.get('price_premium_95')
    price_premium_dt = item.get('price_premium_dt')
    address = item.get('address')

    insert_query = """
    INSERT INTO Gas_stations (station_name, price_100, price_92, price_95, price_spbt, price_dt,
    price_metan, price_premium_92, price_premium_95, price_premium_dt, address)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (station_name, price_100, price_92, price_95, price_spbt, price_dt,
                                  price_metan, price_premium_92, price_premium_95, price_premium_dt, address))

conn.commit()
cursor.close()
conn.close()
