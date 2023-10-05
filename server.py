from flask import Flask, request, jsonify, url_for
from monet_model import monet_style
from vangogh_model import vangogh_style
from ukiyoe_model import ukiyoe_style
from cezanne_model import cezanne_style
from PIL import Image
from waitress import serve

app = Flask(__name__)


@app.route("/all", methods=['POST'])
def all():
    f = request.files['upload_all']
    if f.filename != "":
        monet_style(f)
        vangogh_style(f)
        cezanne_style(f)
        ukiyoe_style(f)

        style_monet_image_path = "results/style_monet_pretrained/test_latest/images/image_fake.png"
        style_vangogh_image_path = "results/style_vangogh_pretrained/test_latest/images/image_fake.png"
        style_cezanne_image_path = "results/style_cezanne_pretrained/test_latest/images/image_fake.png"
        style_ukiyoe_image_path = "results/style_ukiyoe_pretrained/test_latest/images/image_fake.png"

        img_monet = Image.open(style_monet_image_path)
        img_vangogh = Image.open(style_vangogh_image_path)
        img_cezanne = Image.open(style_cezanne_image_path)
        img_ukiyoe = Image.open(style_ukiyoe_image_path)

        img_monet.save("static/results/style_monet_pretrained/test_latest/images/image_fake.png", 'PNG')
        img_vangogh.save("static/results/style_vangogh_pretrained/test_latest/images/image_fake.png", 'PNG')
        img_cezanne.save("static/results/style_cezanne_pretrained/test_latest/images/image_fake.png", 'PNG')
        img_ukiyoe.save("static/results/style_ukiyoe_pretrained/test_latest/images/image_fake.png", 'PNG')

        style_monet_image_url = url_for('static', filename=style_monet_image_path, _external=True)
        style_vangogh_image_url = url_for('static', filename=style_vangogh_image_path, _external=True)
        style_cezanne_image_url = url_for('static', filename=style_cezanne_image_path, _external=True)
        style_ukiyoe_image_url = url_for('static', filename=style_ukiyoe_image_path, _external=True)

        return jsonify({
            'image_monet_url': style_monet_image_url,
            'image_vangogh_url': style_vangogh_image_url,
            'image_cezanne_url': style_cezanne_image_url,
            'image_ukiyoe_url': style_ukiyoe_image_url
        })
    
@app.route("/Monet", methods=['POST'])
def Monet():
    f = request.files['upload_Monet']
    if f.filename != "":
        monet_style(f)

        style_monet_image_path = "results/style_monet_pretrained/test_latest/images/image_fake.png"

        img_monet = Image.open(style_monet_image_path)

        img_monet.save("static/results/style_monet_pretrained/test_latest/images/image_fake.png", 'PNG')

        style_monet_image_url = url_for('static', filename=style_monet_image_path, _external=True)

        return jsonify({
            'image_url': style_monet_image_url
        })
    
@app.route("/Vangogh", methods=['POST'])
def Vangogh():
    f = request.files['upload_Vangogh']
    if f.filename != "":
        vangogh_style(f)

        style_vangogh_image_path = "results/style_vangogh_pretrained/test_latest/images/image_fake.png"

        img_vangogh = Image.open(style_vangogh_image_path)

        img_vangogh.save("static/results/style_vangogh_pretrained/test_latest/images/image_fake.png", 'PNG')

        style_vangogh_image_url = url_for('static', filename=style_vangogh_image_path, _external=True)

        return jsonify({
            'image_url': style_vangogh_image_url
        })
    
@app.route("/Cezanne", methods=['POST'])
def Cezanne():
    f = request.files['upload_Cezanne']
    if f.filename != "":
        cezanne_style(f)

        style_cezanne_image_path = "results/style_cezanne_pretrained/test_latest/images/image_fake.png"

        img_cezanne = Image.open(style_cezanne_image_path)

        img_cezanne.save("static/results/style_cezanne_pretrained/test_latest/images/image_fake.png", 'PNG')

        style_cezanne_image_url = url_for('static', filename=style_cezanne_image_path, _external=True)

        return jsonify({
            'image_url': style_cezanne_image_url
        })
    
@app.route("/Ukiyoe", methods=['POST'])
def Ukiyoe():
    f = request.files['upload_Ukiyoe']
    if f.filename != "":
        ukiyoe_style(f)

        style_ukiyoe_image_path = "results/style_ukiyoe_pretrained/test_latest/images/image_fake.png"

        img_ukiyoe = Image.open(style_ukiyoe_image_path)

        img_ukiyoe.save("static/results/style_ukiyoe_pretrained/test_latest/images/image_fake.png", 'PNG')

        style_ukiyoe_image_url = url_for('static', filename=style_ukiyoe_image_path, _external=True)

        return jsonify({
            'image_url': style_ukiyoe_image_url
        })
    

    
if __name__ == "__main__":
    app.run(debug=True)
    
def create_app():
    return app

