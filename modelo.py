import sqlite3
from datetime import datetime, timedelta


DB_NAME = 'notas.db'
TIMEZONE_OFFSET = 2  # Ajusta la diferencia horaria según tus necesidades (por ejemplo, +2 horas)

def create_table():
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()

        # Crear la tabla solo si no existe
        cur.execute("CREATE TABLE IF NOT EXISTS notas (id INTEGER PRIMARY KEY, codigo TEXT NOT NULL, texto TEXT NOT NULL, fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        con.commit()

        print("Tabla 'notas' creada o ya existente.")

    except sqlite3.Error as e:
        print("Error:", e)
    finally:
        con.close()


create_table()


def save_note(codigo, texto):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    # Obtener la fecha y hora actual con la zona horaria ajustada
    now_with_timezone = datetime.utcnow() + timedelta(hours=TIMEZONE_OFFSET)

    cur.execute("INSERT INTO notas (codigo, texto, fecha_creacion) VALUES (?, ?, ?)", (codigo, texto, now_with_timezone))
    con.commit()
    con.close()


def read_note(codigo):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    result = cur.execute("SELECT texto, fecha_creacion FROM notas WHERE codigo=?", (codigo,))
    result = cur.fetchone()
    con.close()

    if result:
        texto, fecha_creacion_str = result

        try:
            # Convertir la cadena a un objeto datetime
            fecha_creacion = datetime.strptime(fecha_creacion_str, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            fecha_creacion = datetime.strptime(fecha_creacion_str, "%Y-%m-%d %H:%M:%S")

        # Formatear la fecha y hora en el formato deseado (año-mes-día hora:minutos:segundos)
        fecha_formateada = fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")

        return texto, fecha_formateada
    else:
        return None, None
def delete_note(codigo):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""DELETE FROM notas WHERE codigo=?""", (codigo,))
    con.commit()
    con.close()

def get_recent_notes(limit=5):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("SELECT codigo, texto FROM notas ORDER BY fecha_creacion DESC LIMIT ?", (limit,))
    result = cur.fetchall()
    con.close()
    return result

def update_note_state(codigo ):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("UPDATE notas SET =? WHERE codigo=?", ( codigo))
    con.commit()
    con.close()
