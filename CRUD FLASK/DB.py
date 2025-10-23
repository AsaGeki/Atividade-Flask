import psycopg2

DB_HOST = "localhost"
DB_NAME = "ATIVIDADE 18/09"
DB_USER = "postgres"
DB_PASS = "@314159"

connect = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

def get_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn


connect.commit()
connect.close()
