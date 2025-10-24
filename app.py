# app.py
from flask import Flask, request, jsonify, send_from_directory
import json, os, datetime

app = Flask(__name__, static_folder='public')

DB = 'database.json'
if not os.path.exists(DB):
    with open(DB,'w') as f:
        json.dump([], f)

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    with open(DB,'r+') as f:
        data = json.load(f)
        data.append({'email': email, 'password': password, 'ts': datetime.datetime.utcnow().isoformat()})
        f.seek(0); json.dump(data, f, indent=2); f.truncate()
    return 'OK'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def static(path):
    return send_from_directory('public', path or 'index.html')

if __name__ == '__main__':
    app.run(port=5000)
