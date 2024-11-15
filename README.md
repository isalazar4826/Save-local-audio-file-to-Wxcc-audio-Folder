
# Audio Uploader for Webex CC

Este proyecto es una aplicación web simple basada en Flask que permite subir archivos de audio desde una computadora local a la carpeta de audios de Webex Contact Center (Webex CC).

## Características

- Carga archivos de audio en formato WAV.
- Genera un `blobId` único y metadatos asociados para cada archivo.
- Envía la información y el archivo de audio a la API de Webex CC.
- Muestra mensajes de éxito o error al usuario según el resultado de la operación.

## Requisitos previos

- **Python 3.8 o superior**
- **Pip** instalado en tu entorno.
- Clave secreta para la aplicación Flask (definida en `app.secret_key`).
- Token de autenticación de Webex CC válido.

## Instalación

1. Clona este repositorio o descarga el código fuente.
   ```bash
   git clone https://github.com/tu-repositorio/audio-uploader-webex.git
   cd audio-uploader-webex
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install flask requests
   ```

3. Configura la clave secreta y el token de autenticación:
   - Modifica el valor de `app.secret_key` con una clave segura.
   - Actualiza el valor del token en la variable `HEADERS` en el archivo principal.

## Uso

1. Inicia la aplicación Flask:
   ```bash
   python app.py
   ```

2. Abre tu navegador web y navega a `http://127.0.0.1:5000/`.

3. Selecciona un archivo de audio desde tu computadora y súbelo utilizando el formulario.

## Configuración

- **API Endpoint:**  
  El endpoint para la API de Webex CC está definido en la variable `URL`. Asegúrate de que este sea el endpoint correcto para tu organización.

- **Token de Autenticación:**  
  Reemplaza el valor del token en la variable `HEADERS` con un token válido de Webex CC.

- **Timeout de la Solicitud:**  
  El tiempo de espera para las solicitudes HTTP está configurado en 10 segundos. Puedes ajustarlo en la función `requests.post()`.

## Archivos Importantes

- **`app.py`:** Archivo principal con la lógica de la aplicación.
- **`templates/upload.html`:** Plantilla HTML para el formulario de subida.

## Notas de Seguridad

- **Clave secreta:**  
  Asegúrate de usar una clave secreta segura para `app.secret_key` en producción.

- **Token de autenticación:**  
  Nunca expongas tu token de autenticación en un repositorio público. Considéralo información confidencial.

- **Archivos subidos:**  
  Este ejemplo no realiza validaciones avanzadas de los archivos subidos. Considera agregar verificaciones para evitar la carga de archivos maliciosos.

## Contribuciones

Si deseas contribuir, abre un *pull request* o reporta problemas en la sección de *issues*.

---

**Licencia:** MIT  
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
