
# Flask Application for Uploading Audio Files to Webex CC

This is a Python-based Flask application that allows users to upload local audio files from their computer to the Webex CC audio files repository.

## Features

- **File Upload Interface**: Provides a web interface to upload `.wav` audio files.
- **Webex CC Integration**: Sends the uploaded files to the Webex CC audio file repository.
- **Real-Time Feedback**: Displays success or error messages based on the upload result.

## Prerequisites

1. **Python Environment**:
   - Python 3.x installed.
2. **Dependencies**:
   - Flask
   - Requests

   You can install these dependencies by running:
   ```bash
   pip install flask requests
   ```
3. **Webex CC API Access**:
   - An API token with necessary permissions.
   - Replace the placeholder API token and organization ID in the script with your credentials.

## Setup Instructions

1. **Clone or Download** the repository to your local machine.
2. **Replace the Placeholder Values** in the code:
   - `app.secret_key`: Update to a secure secret key.
   - `HEADERS['Authorization']`: Replace with your Webex CC API token.
   - `URL`: Ensure the URL matches the Webex CC endpoint for your organization.
3. **Run the Application**:
   Execute the following command in your terminal:
   ```bash
   python app.py
   ```
4. **Access the Application**:
   Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Visit the home page of the application.
2. Click "Choose File" and select a `.wav` audio file from your computer.
3. Click the "Upload" button to submit the file.
4. Receive feedback about the upload status:
   - Success: Displays the file name and ID from Webex CC.
   - Failure: Displays an error message with the HTTP status code or exception details.

![image](https://github.com/user-attachments/assets/8a2bddc6-ce6c-4196-9462-b16a8ed5a340)

## Notes

- The application is configured to accept `.wav` files. Modify the `contentType` parameter in the code if you need to handle other formats.
- Ensure your API token is valid and has not expired. Refresh it if necessary.

## Disclaimer

This application is for demonstration purposes only. Do not use it in production without securing sensitive credentials and testing thoroughly.


