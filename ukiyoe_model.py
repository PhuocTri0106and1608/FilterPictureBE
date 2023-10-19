import subprocess
from PIL import Image
import os

def ukiyoe_style(image):
    img = Image.open(image)
    file_name = image.filename.rsplit(".", 1)[0] + ".png"
    img.save("datasets/images/{}".format(file_name), 'PNG')
    command = "python test.py --dataroot datasets/images --name style_ukiyoe_pretrained --model test --no_dropout --gpu_ids -1"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
        os.remove(os.path.join('datasets/images/', file_name))
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")