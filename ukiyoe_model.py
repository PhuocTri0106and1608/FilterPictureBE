import subprocess
from PIL import Image
import os

def ukiyoe_style(image):
    img = Image.open(image)
    file_name = image.filename.rsplit(".", 1)[0] + ".png"
    destination = 'datasets/images/' + file_name
    img.save(destination, 'PNG')
    command = "python test.py --dataroot datasets/images --name style_ukiyoe_pretrained --model test --no_dropout --gpu_ids -1"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")