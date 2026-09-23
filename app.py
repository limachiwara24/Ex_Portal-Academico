from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'portal_academico_2026'

usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "pedro": "2026"
}

cursos = [
    {"nombre": "Programación Web", "docente": "Luis Pérez", "cupos": 15},
    {"nombre": "Bases de Datos", "docente": "Ana López", "cupos": 8},
    {"nombre": "Redes", "docente": "Carlos Ruiz", "cupos": 10},
    {"nombre": "Inteligencia Artificial", "docente": "Marta Díaz", "cupos": 5}
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/cursos')
def lista_cursos():
    return render_template('cursos.html', cursos=cursos)


@app.route('/perfil')
def perfil():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('perfil.html', usuario=session['usuario'])


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)