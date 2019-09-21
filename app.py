from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)#es la aplicacion en el servidor y se delega a una variable 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseDeDatos/tasks.db'
db = SQLAlchemy(app)#crea un cursor a la base de datos

class task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    contenido = db.Column(db.String(200))
    hecho = db.Column(db.Boolean)

@app.route('/')#crear una ruta 
def home():#puedes poner cualquier nombre es la ruta inicial
    showData = task.query.all()#pregunta por todos los datos en la base de datos
    return render_template('index.html', tareasguardadas= showData)#llama a los archivos en el carpeta templates 

@app.route('/crear-tarea',methods=['POST'])
def crear():
    tarea = task(contenido=request.form['contenido'],hecho=False)
    db.session.add(tarea)#nos permite agregar contenido a la base de datos
    db.session.commit()#pone fin a la sesion de ingreso de datos
    return redirect(url_for('home'))#redirecciona a una url que queramos en este caso home

@app.route('/hecho/<id>')
def hecho(id):
    tarea = task.query.filter_by(id=int(id)).first()
    tarea.hecho = not(tarea.hecho)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/borrar/<id>')
def borrar(id):
    tarea = task.query.filter_by(id=int(id)).first()
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":#para ejecutarlo se hace una comparacion para saber si es el archivo principal ///// codigo inicil
    app.run(debug=True)#debug para que si se modifica el codigo el servidor se reinicia ///// codigo inicial

