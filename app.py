from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)#es la aplicacion en el servidor y se delega a una variable 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseDeDatos/tasks.db'
db = SQLAlchemy(app)#crea un cursor a la base de datos

@app.route('/')#crear una ruta
def home():#puedes poner cualquier nombre es la ruta inicial
    return render_template('index.html')#llama a los archivos en el carpeta templates
if __name__ == "__main__":#para ejecutarlo se hace una comparacion para saber si es el archivo principal 
    app.run(debug=True)#debug para que si se modifica el codigo el servidor se reinicia

