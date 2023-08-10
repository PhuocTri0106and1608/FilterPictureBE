from flask import Flask, request, send_file
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
        style_image = model(f)
        # uploaded_file_path = "datasets/images/"+f.filename
        # f.save(uploaded_file_path)
        # command = "python monet_model.py"
        # try:
        #     subprocess.run(command, shell=True, check=True)
        #     print("Command executed successfully.")
        # except subprocess.CalledProcessError as e:
        #     print(f"Command execution failed: {e}")
        # filename_fake = f.filename[:-4] + "_fake" + f.filename[-4:]
        # style_image_path = "results/style_monet_pretrained/test_latest/images/" + filename_fake
        # style_image = plt.imread(style_image_path)
        # os.remove(uploaded_file_path)
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

