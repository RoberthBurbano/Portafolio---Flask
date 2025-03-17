from flask import Flask, render_template
from flask import Flask, send_from_directory,url_for

app = Flask(__name__)

@app.route('/')
def index():
    datos_personales = {
        "nombre": "Roberth Dario Burbano Romo",
        "edad": 27,
        "ubicacion": "Pasto, Colombia",
        "correo": "burbanoroberth@gmail.com",
        "telefono": "+57 3203815636"
    }

    intereses = [
        "Desarrollo de Software",
        "Inteligencia Artificial",
        "Ciberseguridad",
        "Blockchain",
        "Automatización de Procesos",
        "Análisis de Datos"
    ]

    return render_template('index.html', 
                           name=datos_personales["nombre"], 
                           datos_personales=datos_personales, 
                           intereses=intereses, 
                           bio="Sobre mí", 
                           profile_pic="static/img/dario.jpg")


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('static/files', filename)



if __name__ == '__main__':
    app.run(debug=True)
app.run(debug=True)