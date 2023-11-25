import psycopg2

def get_data_by_id(id_value):
    dbname = "rasa_bots"
    user = "postgres"
    password = "1511"
    host = "localhost"
    port = "5432"
    table_name = 'gas_stations'
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        cursor = connection.cursor()

        query = f"SELECT * FROM {table_name} WHERE id = %s"
        cursor.execute(query, (id_value,))
        data = cursor.fetchone()

        return data

    except psycopg2.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


id_value = 1
data = get_data_by_id(id_value)

if data:
    print(data)