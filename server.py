from flask import Flask, request, jsonify, url_for, send_file
import os
from monet_model import monet_style
from vangogh_model import vangogh_style
from ukiyoe_model import ukiyoe_style
from cezanne_model import cezanne_style
from PIL import Image
import subprocess
import matplotlib.pyplot as plt
from waitress import serve

app = Flask(__name__)


@app.route("/monet", methods=['POST'])
def monet():
    f = request.files['upload_monet']
    if f.filename != "":
        monet_style(f)
        style_image_path = "results/style_monet_pretrained/test_latest/images/image_fake.png"
        img = Image.open(style_image_path)
        img.save("static/results/style_monet_pretrained/test_latest/images/image_fake.png", 'PNG')
        style_image_url = url_for('static', filename=style_image_path, _external=True)
        return jsonify({'image_url': style_image_url})

@app.route("/vangogh", methods=['POST'])
def vangogh():
    f = request.files['upload_vangogh']
    if f.filename != "":
        vangogh_style(f)
        style_image_path = "results/style_vangogh_pretrained/test_latest/images/image_fake.png"
        img = Image.open(style_image_path)
        img.save("static/results/style_vangogh_pretrained/test_latest/images/image_fake.png", 'PNG')
        style_image_url = url_for('static', filename=style_image_path, _external=True)
        return jsonify({'image_url': style_image_url})

@app.route("/cezanne", methods=['POST'])
def cezanne():
    f = request.files['upload_cezanne']
    if f.filename != "":
        cezanne_style(f)
        style_image_path = "results/style_cezanne_pretrained/test_latest/images/image_fake.png"
        img = Image.open(style_image_path)
        img.save("static/results/style_cezanne_pretrained/test_latest/images/image_fake.png", 'PNG')
        style_image_url = url_for('static', filename=style_image_path, _external=True)
        return jsonify({'image_url': style_image_url})
    
@app.route("/ukiyoe", methods=['POST'])
def ukiyoe():
    f = request.files['upload_ukiyoe']
    if f.filename != "":
        ukiyoe_style(f)
        style_image_path = "results/style_ukiyoe_pretrained/test_latest/images/image_fake.png"
        img = Image.open(style_image_path)
        img.save("static/results/style_ukiyoe_pretrained/test_latest/images/image_fake.png", 'PNG')
        style_image_url = url_for('static', filename=style_image_path, _external=True)
        return jsonify({'image_url': style_image_url})
    
if __name__ == "__main__":
    app.run(debug=True)
    
def create_app():
    return app

