from flask import Flask, render_template, request, redirect, url_for
import secrets
import string
from datetime import datetime
from modelo import create_table, save_note, delete_note, read_note

BASE_URL = 'http://localhost:5000/'

app = Flask(__name__)

notas = {}



@app.route('/', methods=['GET', 'POST'])
def crearnota():
    if request.method == 'POST':
        texto = request.form.get('texto')

        if texto != '':
            id_nota = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(20))
            url_nota = url_for('enlace', codigo=id_nota, _external=True)
            fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_note(id_nota, texto)
            codigo = id_nota
            enlace = BASE_URL + 'nota/' + codigo
            return redirect(url_for('enlace', codigo=id_nota))
        else:
            return render_template('crearnota.html')
    else:
        return render_template('crearnota.html')
   


@app.route('/enlace/<codigo>')
def enlace(codigo):
    url_nota = url_for('leernota',  codigo=codigo)
    return render_template('enlace.html', url_nota=url_nota, codigo=codigo)



@app.route('/leernota/<codigo>')
def leernota(codigo):
    # Leer la nota correspondiente al código desde la base de datos
    nota = read_note(codigo)
    delete_note(codigo) 
    # Renderizar la plantilla leernota.html y pasar la nota como argumento
    return render_template('leernota.html', nota=nota)


if __name__ == '__main__':
    app.run(debug=True)
               