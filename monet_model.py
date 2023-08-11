import subprocess
import matplotlib.pyplot as plt
from PIL import Image
import os

def model(image):
    # uploaded_file_path = "./opt/render/project/src/datasets/images/"+image.filename
    image.filename = "image.png"
    uploaded_file_path = "./opt/render/project/src/datasets/images/image.png"
    image.save(uploaded_file_path)
    command = "python test.py --dataroot datasets/images --name style_monet_pretrained --model test --no_dropout --gpu_ids -1"
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
        # os.remove(uploaded_file_path)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")