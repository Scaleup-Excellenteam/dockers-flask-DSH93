from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Temporary directory to save code files
TEMP_DIR = 'temp_code'

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

@app.route('/upload', methods=['POST'])
def upload_code():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    file_path = os.path.join(TEMP_DIR, file.filename)
    file.save(file_path)
    print(f'File saved to {file_path}')
    return jsonify({'message': 'File successfully uploaded', 'file_path': file_path}), 200

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(TEMP_DIR)
    print(f'Files in {TEMP_DIR}: {files}')
    return jsonify({'files': files})

@app.route('/execute', methods=['GET'])
def execute_code():
    language = request.args.get('language')
    filename = request.args.get('filename')
    file_path = os.path.join(TEMP_DIR, filename)
    
    if not os.path.exists(file_path):
        print(f'File {file_path} not found')
        return jsonify({'error': 'File not found'}), 404
    
    # Forward the code to the appropriate language executor
    response = forward_to_executor(language, file_path)
    return jsonify(response)

def forward_to_executor(language, file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    if language == 'python':
        response = requests.post('http://python-executor-container:5001/execute', json={'code': code})
        return response.json()
    elif language == 'java':
        response = requests.post('http://java-executor-container:5002/execute', json={'code': code})
        return response.json()
    elif language == 'dart':
        response = requests.post('http://dart-executor-container:5003/execute', json={'code': code})
        return response.json()
    else:
        return {'message': f'Code execution for {language} not implemented'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
