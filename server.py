from flask import Flask, request, jsonify, url_for, send_file
import os
from monet_model import monet_style
from vangogh_model import vangogh_style
from ukiyoe_model import ukiyoe_style
from cezanne_model import cezanne_style
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
        # protocol = request.headers.get('X-Forwarded-For', request.scheme)
        # style_image_url = url_for('static', filename=style_image_path, _external=True)
        # return jsonify({'image_url': style_image_url})
        style_image = plt.imread(style_image_path)
        fig = plt.figure()
        plt.imshow(style_image)
        plt.axis('off')
        plt.savefig('result.png')
        plt.close(fig)
        return send_file('result.png', mimetype='image/png')

@app.route("/vangogh", methods=['POST'])
def vangogh():
    f = request.files['upload_vangogh']
    if f.filename != "":
        vangogh_style(f)
        style_image_path = "results/style_vangogh_pretrained/test_latest/images/image_fake.png"
        style_image = plt.imread(style_image_path)
        fig = plt.figure()
        plt.imshow(style_image)
        plt.axis('off')
        plt.savefig('result.png')
        plt.close(fig)
        return send_file('result.png', mimetype='image/png')

@app.route("/cezanne", methods=['POST'])
def cezanne():
    f = request.files['upload_cezanne']
    if f.filename != "":
        cezanne_style(f)
        style_image_path = "results/style_cezanne_pretrained/test_latest/images/image_fake.png"
        style_image = plt.imread(style_image_path)
        fig = plt.figure()
        plt.imshow(style_image)
        plt.axis('off')
        plt.savefig('result.png')
        plt.close(fig)
        return send_file('result.png', mimetype='image/png')
    
@app.route("/ukiyoe", methods=['POST'])
def ukiyoe():
    f = request.files['upload_ukiyoe']
    if f.filename != "":
        ukiyoe_style(f)
        style_image_path = "results/style_ukiyoe_pretrained/test_latest/images/image_fake.png"
        style_image = plt.imread(style_image_path)
        fig = plt.figure()
        plt.imshow(style_image)
        plt.axis('off')
        plt.savefig('result.png')
        plt.close(fig)
        return send_file('result.png', mimetype='image/png')
    
if __name__ == "__main__":
    app.run(debug=True)
    
def create_app():
    return app

