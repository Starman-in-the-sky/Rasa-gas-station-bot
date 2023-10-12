import psycopg2

def get_addresses():
    dbname = "rasa_bots"
    user = "postgres"
    password = "1511"
    host = "localhost"
    port = "5432"

    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        cursor = connection.cursor()

        cursor.execute("SELECT address FROM gas_stations")
        addresses = [row[0] for row in cursor.fetchall()]

        return addresses

    except psycopg2.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

addresses = get_addresses()

if addresses:
    for address in addresses:
        print(address)
