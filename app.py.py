import json
import time
from flask import Flask, request, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave secreta más segura

# Configuración
URL = "https://api.wxcc-us1.cisco.com/organization/d9cd7ecf-e6e1-49fb-ab07-a69cb49ea081/audio-file"
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiJ9.eyJjbHVzdGVyIjoiUDBBMSIsInByaXZhdGUiOiJleUpqZEhraU9pSktWMVFpTENKbGJtTWlPaUpCTVRJNFEwSkRMVWhUTWpVMklpd2lZV3huSWpvaVpHbHlJbjAuLkhaMUdnSkRxc3BCNjk2cmFKWGJxUWcuVW01dGdoY1U3blBqX2dHdkdKWmI3eXBReVYxVWhaRWY0VVlFV3ljVjFGQTMxM1ROMHRvVlpFYjQyUlpsOFFvOHR0ekJ0elNKLXdFTDdKSFhoaFE3Q2ZIVzNwQVRKc2xHVWlSX2IybGdwRmIzWXl1UzYxYWI3ZHptMUk2UURETUVQRlFlNEktYjJwS1B1Y2E2UGgxMlBCY1YtNWhjQ0l6dlJDV01ub2RwUTMxZWpKWkVFeUEyaU5Xa2VoNUxIYVZyTi1nX0tRX21peGlDYTlTZTVmWHNHWjVNNjZJckhHT1FmSkUxRUM3ZTYyTHlxQTR4LWZlNTNnWEtBNVBoZ3ROM3VsX1pOTGtHOWl4RlRZRlBYeU5JV0hiTWk2T1g2akZfSWNVWThuRy1sMUIxOHUzMHM3akQwOXU1NWpfSGtEMXZEV01kcThkTW00eGdvbWV1N1EybllLSzlvYzVpRUhVbGRONUNCb1A4RkFaWm15X2FwNjVPLV93R2R6T1dSc2tfcWUyU1RrREpyNW9xLUxuaGxOcDEyVlUyYnhwc3pXLWdCTmhpVERETUJXa09sU3VYSnhFS0J2bmJtZW9EYzhXbmUxd0NtdlBvMUZyaDRmUzFFX0lfLU9CZ0VrbTNpSTlxYzkxZnlrVUw2NGxaUXUzeWpxSEY3MGoxb3BkUmhOdlVCRkFuZUpHc0lLV2U4Zk04TkdmSXhkUEh4QmxCNnExSjVBbm9GX3dPd0I5di05eUlteURyaUZsM2g1akRId1ktMWFzQU1nRk50VHU3a1R5S0lER0lVT1VWRWRHTm1YbHZHemRtTDlkYzJaWl9ZVUhUNzROT0VoVjZIQTVWQVRJXzBuamx4OENPeE4tNVJZRnd6azVnNUxMYTlBQU5wS1dlVkNaTjNZTHNOc0VXTW44WHBYMnpkakprV3p1dnBjU1ViM3VnMGZTWEo1ek9WbW1lZllpdUh1WW1MOXpyTTg1QS1CQzFQQTlkNURlUnVRRUZJZVQybUdaWGJCcHJaRlN4dk9jdGZ4TnM2QnhpTHlqWTYtMHZ2Nl9oNnQwSGZNZ1VGRWhkSEEwVE5NT2F5WEx6X09pQktFdEFSeWdFNXNtY0VZVkZkRlRUUEN3eS1OU2VNX1NHdUstMTExeTl3UFdXeXpQNlpIODZWbWxiS1VQcjJuLXBvN0FmbHlMdm1INGZwTWtsWEtmSXlybFRDOHJhTEI0bWd0X0h5eG1mNmxSSERGRnNubmpVSkRXQUxwUzRyYmFNRDhRYnRnRmZTRWZyOVlvMHRrOURlLVNrc0taOVk1cUh0THAxOHhxWE5DbTFPZDIxQ1k5Mnl0c0NCX2ZiOUdBWjZwT1Z5TFliWDIzQ0c3TUhfb1Z6U0xIakxoeW9ZXzZVTFI3ellwbmlfWjdpTXlSMnhNMm9jTVpZNS02dVIwTzBPMS1sdEdpeEJNQkpKWWtMdTBISHVSZmtzQXJYdGh6azVYcEFPY0diVURpb2FaZnM0OEN4RnE1XzhaY0FUY2w4aldlRDA0SlA3MXlpNV91YVlNNk1VVFdtcXh5c2JjZFRqTjMxWnNHcll1TTJjRi1QMXZaN0s2ajI1T3RkMzN0eVM5TEJUc1dKMXBvRC5BSHY0T1hJTWhvTHVMRHZoQjBONXFBIiwidXNlcl90eXBlIjoidXNlciIsInRva2VuX2lkIjoiQWFaM3IwWkRBNE0yVm1ZVFV0TVdNM1lpMDBNakJsTFdFMllUSXRZbVpoT1daalltTmhZell3TlRobVlXTXlZVE10T0RZMiIsInJlZmVyZW5jZV9pZCI6IjQ5MDQxY2UwLTQ0YWUtNDgyYS04YWIyLTZjNTU3YzZlYjc0MiIsImlzcyI6Imh0dHBzOlwvXC9pZGJyb2tlci1iLXVzLndlYmV4LmNvbVwvaWRiIiwidXNlcl9tb2RpZnlfdGltZXN0YW1wIjoiMjAyNDExMTUwNDI2NDMuNDc4WiIsInJlYWxtIjoiZDljZDdlY2YtZTZlMS00OWZiLWFiMDctYTY5Y2I0OWVhMDgxIiwiY2lzX3V1aWQiOiI5ZGI1ZjlhYy00MmUwLTRlMTItOGZjZC1hNGRjMWNjNzFiMDQiLCJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiZXhwaXJ5X3RpbWUiOjE3MzE3MDk2MDQ5MDksImNsaWVudF9pZCI6IkM1ODI1NGYzOGNlMDBlYzdhZmQxYjYwNjZmOTdlM2MyNjgwZjgxOWZhZWZlNjhhOTY1MjE5N2EzYTllMTg4N2M0In0.QOnsMfokzp2TzUDCKDsPfX0qtHhae-4DsaYU_yJFQ7yriLAMTlZL1ez7ox2CSh6U5GXSGQIjSxEp-LydcbqCZXbGft_0tiBtOkmbrOTdRsagduA2l5WG0UGNWXNKXJ0bSzpwOm8awyye62GGjNQo0NE9HB2XSZi_pqJlpGAqWwZAvXi8T1GDKu-78x0boQVZhD1qdrdwkdSQEuF0MpKMIdl2I4tlb3pf4ZmPZNWv9GwfXbZlBDaSs7-vnOyF9C6XixtTdPxPEYk8KPe0040bciVDb9D1lqlGxc3Wu0_c33t6XeLHhEW0oFMYuqDkVXVX6xpKNmBQAPHsk_MHpSuZjw",  # Cambia esto por tu token
}

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
