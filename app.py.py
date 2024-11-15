import json
import time
from flask import Flask, request, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave secreta más segura

# Configuración
URL = "https://api.wxcc-us1.cisco.com/organization/{{YOUR ORG ID }}/audio-file"
HEADERS = {
    "Authorization": "Bearer {{ Your TOKEN }} "
@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio_file' not in request.files:
        flash('No se ha seleccionado ningún archivo.')
        return redirect(request.url)

    audio_file = request.files['audio_file']

    if audio_file.filename == '':
        flash('No se ha seleccionado ningún archivo.')
        return redirect(request.url)

    # Preparar la información del archivo
    audio_file_info = {
        "blobId": f"audio-file_{time.strftime('%Y%m%d%H%M%S')}",  # Generar un nuevo blobId único
        "contentType": "AUDIO_WAV",
        "createdTime": int(time.time() * 1000),
        "name": audio_file.filename,
        "organizationId": "d9cd7ecf-e6e1-49fb-ab07-a69cb49ea081",
        "version": 0
    }

    try:
        files = {
            "audioFile": (audio_file.filename, audio_file.stream, "audio/wav"),  # Ajustar el tipo MIME
            "audioFileInfo": (None, json.dumps(audio_file_info), "application/json")
        }

        # Enviar la solicitud POST
        response = requests.post(URL, headers=HEADERS, files=files, timeout=10)

        if response.status_code == 200 or response.status_code == 201:
            response_data = response.json()  # Convierte la respuesta a un diccionario
            flash(f'Archivo de audio cargado correctamente: {response_data["name"]} (ID: {response_data["id"]})')
        else:
            flash(f'Error al cargar el archivo: {response.status_code}')

    except requests.exceptions.RequestException as e:
        flash(f'Error en la solicitud: {str(e)}')

    return redirect(url_for('upload_form'))

if __name__ == '__main__':
    app.run(debug=True)
