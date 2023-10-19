from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from monet_model import monet_style
from vangogh_model import vangogh_style
from ukiyoe_model import ukiyoe_style
from cezanne_model import cezanne_style
from PIL import Image
from waitress import serve
import os

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"], "headers": ["Content-Type", "Authorization"]}})

    
@app.route("/Monet", methods=['POST'])
def Monet():
    try:
        f = request.files['upload_Monet']
        if f.filename != "":
            monet_style(f)

            file_name = f.filename.rsplit(".", 1)[0] + ".png"
            fake_file_name = f"{file_name.split('.')[0]}_fake.{file_name.split('.')[1]}"

            style_monet_image_path = 'results/style_monet_pretrained/test_latest/images/' +  fake_file_name

            img_monet = Image.open(style_monet_image_path)

            static_path = 'static/results/style_monet_pretrained/test_latest/images/' + fake_file_name

            img_monet.save(static_path, 'PNG')

            style_monet_image_url = url_for('static', filename=style_monet_image_path, _external=True)


            return jsonify({
                'image_url': style_monet_image_url
            })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })
    
@app.route("/Vangogh", methods=['POST'])
def Vangogh():
    try:
        f = request.files['upload_Vangogh']
        if f.filename != "":
            vangogh_style(f)

            file_name = f.filename.rsplit(".", 1)[0] + ".png"
            fake_file_name = f"{file_name.split('.')[0]}_fake.{file_name.split('.')[1]}"

            style_vangogh_image_path = 'results/style_vangogh_pretrained/test_latest/images/' +  fake_file_name

            img_vangogh = Image.open(style_vangogh_image_path)

            static_path = 'static/results/style_vangogh_pretrained/test_latest/images/' + fake_file_name

            img_vangogh.save(static_path, 'PNG')

            style_vangogh_image_url = url_for('static', filename=style_vangogh_image_path, _external=True)


            return jsonify({
                'image_url': style_vangogh_image_url
            })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })
    
@app.route("/Cezanne", methods=['POST'])
def Cezanne():
    try:
        f = request.files['upload_Cezanne']
        if f.filename != "":
            cezanne_style(f)

            file_name = f.filename.rsplit(".", 1)[0] + ".png"
            fake_file_name = f"{file_name.split('.')[0]}_fake.{file_name.split('.')[1]}"

            style_cezanne_image_path = 'results/style_cezanne_pretrained/test_latest/images/' +  fake_file_name

            img_cezanne = Image.open(style_cezanne_image_path)

            static_path = 'static/results/style_cezanne_pretrained/test_latest/images/' + fake_file_name

            img_cezanne.save(static_path, 'PNG')

            style_cezanne_image_url = url_for('static', filename=style_cezanne_image_path, _external=True)


            return jsonify({
                'image_url': style_cezanne_image_url
            })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })
    
@app.route("/Ukiyoe", methods=['POST'])
def Ukiyoe():
    try:
        f = request.files['upload_Ukiyoe']
        if f.filename != "":
            ukiyoe_style(f)

            file_name = f.filename.rsplit(".", 1)[0] + ".png"
            fake_file_name = f"{file_name.split('.')[0]}_fake.{file_name.split('.')[1]}"

            style_ukiyoe_image_path = 'results/style_ukiyoe_pretrained/test_latest/images/' +  fake_file_name

            img_ukiyoe = Image.open(style_ukiyoe_image_path)

            static_path = 'static/results/style_ukiyoe_pretrained/test_latest/images/' + fake_file_name

            img_ukiyoe.save(static_path, 'PNG')

            style_ukiyoe_image_url = url_for('static', filename=style_ukiyoe_image_path, _external=True)


            return jsonify({
                'image_url': style_ukiyoe_image_url
            })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })
    

    
if __name__ == "__main__":
    app.run(debug=True)
    
def create_app():
    return app

