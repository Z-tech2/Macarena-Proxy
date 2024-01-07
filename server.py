import os
from flask import Flask, send_from_directory, render_template, redirect
import requests

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        url = request.args['url']
        html = requests.get(url).text
        return html


if __name__ == "__main__":
    app.run(port=port)
