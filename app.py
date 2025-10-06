import os
from flask import Flask, render_template, send_from_directory

# Inicializar la aplicación Flask
app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    # Datos personales
    datos_personales = {
        "nombre": "Roberth Dario Burbano Romo",
        "edad": 27,
        "ubicacion": "Pasto, Colombia",
        "correo": "burbanoroberth@gmail.com",
        "telefono": "+57 3203815636"
    }

    # Lista de intereses
    intereses = [
        "Desarrollo de Software",
        "Inteligencia Artificial",
        "Ciberseguridad",
        "Blockchain",
        "Automatización de Procesos",
        "Análisis de Datos"
    ]

    # Renderizar el template con los datos
    return render_template(
        'index.html',
        name=datos_personales["nombre"],
        datos_personales=datos_personales,
        intereses=intereses,
        bio="Sobre mí",
        profile_pic="img/dario.jpg"  # ya no pongas "static/" aquí
    )

# Ruta para descargar archivos del CV
@app.route('/download/<path:filename>')
def download_file(filename):
    directory = os.path.join(app.root_path, 'static', 'files')
    return send_from_directory(directory, filename, as_attachment=True)

# Punto de entrada de la app
if __name__ == '__main__':
    # Render usa una variable de entorno llamada PORT
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
