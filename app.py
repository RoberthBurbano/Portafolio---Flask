from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
