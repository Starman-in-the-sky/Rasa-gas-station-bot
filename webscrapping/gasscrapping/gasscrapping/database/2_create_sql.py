import psycopg2

host = 'localhost'
port = 5432
user = 'postgres'
password = '1511'
database = 'rasa_bots'


conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password
)


conn.autocommit = True


cursor = conn.cursor()


def database_exists(cursor, database_name):
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (database_name,))
    return cursor.fetchone() is not None

if not database_exists(cursor, database):
    print(f"База данных '{database}' не существует. Создание базы данных.")


    create_database_query = f"CREATE DATABASE {database}"
    cursor.execute(create_database_query)

    print(f"База данных '{database}' создана.")

conn.autocommit = False


cursor.close()
conn.close()
