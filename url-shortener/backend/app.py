from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import redis
import hashlib

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
r = redis.Redis(host='localhost', port=6379, db=0)

def shorten_url(url):
    hash_object = hashlib.md5(url.encode())
    short_url = hash_object.hexdigest()[:6]
    r.set(short_url, url)
    return short_url

@app.after_request
def handle_options(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"
    return response

@app.route('/shorten', methods=['POST'])
def shorten():
    print("shorten called")
    data = request.get_json()
    long_url = data['url']
    short_url = shorten_url(long_url)
    result = jsonify({'short_url': f'http://127.0.0.1:5000/{short_url}'})
    return result

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    long_url = r.get(short_url)
    if long_url:
        return redirect(long_url.decode('utf-8'))
    else:
       
        return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)