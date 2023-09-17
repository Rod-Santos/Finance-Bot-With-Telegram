import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )

def insert_user(user_id, user_name=None):
    conn = connect()
    cur = conn.cursor()
    if user_name:
        cur.execute("INSERT INTO usuarios (id, nome) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", (user_id, user_name))
    else:
        cur.execute("INSERT INTO usuarios (id) VALUES (%s) ON CONFLICT (id) DO NOTHING", (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def insert_despesa(valor, categoria_id, usuario_id):
    conn = connect()
    cur = conn.cursor()
    data_atual = datetime.now().strftime('%Y-%m-%d')
    cur.execute("INSERT INTO despesas (valor, data, categoria_id, usuario_id) VALUES (%s, %s, %s, %s)", (valor, data_atual, categoria_id, usuario_id))
    conn.commit()
    cur.close()
    conn.close()

def get_all_categories():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM categorias")
    categories = cur.fetchall()
    cur.close()
    conn.close()
    return categories
