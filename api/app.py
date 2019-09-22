from flask import Flask, request, escape, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb')
dbApp = client.app;

@app.route("/")
def main():
    name = request.args.get('name', 'World')
    return jsonify({'name': name})

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
