from flask import Flask, request, jsonify, url_for
import os
from monet_model import model
# import vangogh_model
# import ukiyoe_model
# import cezanne_model
import subprocess
import matplotlib.pyplot as plt
from waitress import serve

app = Flask(__name__)


@app.route("/monet", methods=['POST'])
def predict():
    f = request.files['upload']
    if f.filename != "":
        model(f)
        style_image_path = "results/style_monet_pretrained/test_latest/images/image_fake.png"
        protocol = request.headers.get('X-Forwarded-For', request.scheme)
        style_image_url = url_for('static', filename=style_image_path, _external=True, _scheme=protocol)
        return jsonify({'image_url': style_image_url})
    
if __name__ == "__main__":
    app.run(debug=True)
    
def create_app():
    return app

