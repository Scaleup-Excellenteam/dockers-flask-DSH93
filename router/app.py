from flask import Flask, request, jsonify
import os
import requests
import base64

app = Flask(__name__)
CODE_DIR = '/app/code'

os.makedirs(CODE_DIR, exist_ok=True)

@app.route('/submit', methods=['POST'])
def submit_code() -> jsonify:
    """
    Handle the submission of code via a POST request to the /submit endpoint.

    This function retrieves the language and code from the request form data.
    If the code is encoded in base64, it decodes it and converts it to UTF-8.
    The code is then saved to a file in the specified CODE_DIR directory.
    Finally, the function prints the file path and its content, and returns a JSON response.

    Returns:
        A JSON response indicating the status of the code submission.
    """
    
    language = request.form['language']
    code = request.form['code']
    encoding = request.form.get('encoding')

    if encoding == 'base64':
        code = base64.b64decode(code).decode('utf-8') # The code is decoded from base64 and converted to UTF-8
        print(f"Decoded code: {code}")

    file_path = os.path.join(CODE_DIR, f'code.{language}')

    with open(file_path, 'w') as code_file:
        code_file.write(code)

    print(f"File created: {file_path}")
    with open(file_path, 'r') as f:
        print(f"File content: {f.read()}")

    return jsonify({"status": "code submitted successfully"})

@app.route('/execute/<language>', methods=['GET'])
def execute_code(language: str)->jsonify:
    """
    Executes the given code for the specified language.

    Args:
        language (str): The programming language of the code.

    Returns:
        A JSON response containing the result of executing the code.

    Raises:
        404: If no code is found for the specified language.
        400: If the specified language is not supported.
    """

    file_path = os.path.join(CODE_DIR, f'code.{language}')
    if not os.path.exists(file_path):
        return jsonify({"error": "No code found for this language"}), 404

    if language == 'java':
        url = 'http://java-executor:5002/execute'
    elif language == 'python':
        url = 'http://python-executor:5001/execute'
    elif language == 'dart':
        url = 'http://dart-executor:5003/execute'
    else:
        return jsonify({"error": "Unsupported language"}), 400

    with open(file_path, 'r') as code_file: # The code is read from the file
        code = code_file.read()

    response = requests.post(url, json={"code": code}) # The code is sent to the appropriate executor service
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
