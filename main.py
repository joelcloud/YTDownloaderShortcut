from logging import exception
import os
from flask import Flask, jsonify, request, after_this_request, send_file
from api import API

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify(health='alive'), 200

@app.route('/download', methods=['POST'])
def download():
    try:
        video = API.download(request.args.get('v'))
    except Exception as e:
        return jsonify(error=str(e)), 400

    @after_this_request
    def removeFile(response):
        os.remove(video)
        return response
        
    return send_file(video, as_attachment=True), 200

if __name__ == '__main__':
    app.run()