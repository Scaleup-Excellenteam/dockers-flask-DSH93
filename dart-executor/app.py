from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.get_json().get('code')
    if not code:
        return jsonify({'error': 'No code provided'}), 400

    with open('temp_code.dart', 'w') as code_file:
        code_file.write(code)

    try:
        result = subprocess.run(['dart', 'run', 'temp_code.dart'], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = e.stderr

    os.remove('temp_code.dart')
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
