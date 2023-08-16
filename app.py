from flask import Flask, render_template, request, redirect, url_for
import secrets
import string
from datetime import datetime
from qrcode import make as make_qrcode
from modelo import create_table, save_note, delete_note, read_note, get_recent_notes

BASE_URL = 'http://localhost:5000/'

app = Flask(__name__)

def codigo_qr(enlace):
    qr = make_qrcode(enlace)
    qr_image_path = f"static/qrcode.png"
    qr.save(qr_image_path)
    return qr_image_path

@app.route('/', methods=['GET', 'POST'])
def crearnota():
    if request.method == 'POST':
        texto = request.form.get('texto') 
        if texto:
            id_nota = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(20))
            save_note(id_nota, texto)
            return redirect(url_for('enlace', codigo=id_nota))

    return render_template('crearnota.html')

@app.route('/enlace/<codigo>')
def enlace(codigo):
    url_nota = url_for('leernota', codigo=codigo)
    qr = codigo_qr(url_nota)
    return render_template('enlace.html', url_nota=url_nota, codigo=codigo, qr_image_path=qr)

@app.route('/leernota/<codigo>')
def leernota(codigo):
    # Leer la nota correspondiente al código desde la base de datos
    texto, fecha_creacion = read_note(codigo)
    delete_note(codigo)
    
    # Crear un diccionario con las claves adecuadas para la plantilla
    nota = {
        'texto': texto,
        'fecha_creacion': fecha_creacion
    }
    
    # Renderizar la plantilla leernota.html y pasar la nota como argumento
    return render_template('leernota.html', nota=nota)

@app.route('/historial', methods=['GET', 'POST'])
def historial():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        return redirect(url_for('ver_historial', codigo=codigo))

    return render_template('historial.html')

@app.route('/ver_historial/<codigo>')
def ver_historial(codigo):
    # Obtener las notas correspondientes al código del historial
    notas = get_recent_notes()
    return render_template('ver_historial.html', notas=notas)

if __name__ == '__main__':
    create_table()  # Crear la tabla antes de ejecutar la aplicación
    app.run(debug=True)
