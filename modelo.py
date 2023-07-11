import sqlite3
from datetime import datetime

DB_NAME = 'notas.db'
fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def create_table():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS notas (
        codigo CHAR(42) PRIMARY KEY,
        texto TEXT NOT NULL,
        fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP());
        """
    )
    con.close()

def save_note(codigo, texto):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("INSERT INTO notas (codigo, texto) VALUES (?, ?)", (codigo, texto))
    con.commit()
    con.close()

def read_note(codigo):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    result = cur.execute("SELECT codigo, texto FROM notas WHERE codigo=?", (codigo,))
    result = cur.fetchone()
    con.close()
    if result:
        _, texto = result  # Extraer el texto de la tupla
        return texto
    else:
        return None


def delete_note(codigo):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""  DELETE FROM notas WHERE codigo=?""", (codigo,))
    con.commit()
    con.close()
