from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder = 'templates')
CORS(app)

def rot18(text):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        elif 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif '0' <= char <= '9':
            result.append(chr((ord(char) - ord('0') + 5) % 10 + ord('0')))
        else:
            result.append(char)
    return ''.join(result)

@app.route('/')
def index():
    return render_template('fronti.html')

@app.route('/rot18', methods=['POST'])
def handle_rot18():
    data = request.get_json()
    text = data.get('text', '')
    encrypted_text = rot18(text)
    return jsonify({'result': encrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
