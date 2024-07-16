from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.get_json().get('code')
    if not code:
        return jsonify({'error': 'No code provided'}), 400

    with open('TempCode.java', 'w') as code_file:
        code_file.write(code)

    try:
        compile_result = subprocess.run(['javac', 'TempCode.java'], capture_output=True, text=True)
        if compile_result.returncode != 0:
            return jsonify({'output': compile_result.stderr})

        run_result = subprocess.run(['java', 'TempCode'], capture_output=True, text=True)
        output = run_result.stdout
    except subprocess.CalledProcessError as e:
        output = e.stderr

    os.remove('TempCode.java')
    os.remove('TempCode.class')
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
