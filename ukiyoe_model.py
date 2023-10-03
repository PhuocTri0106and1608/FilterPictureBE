import subprocess
from PIL import Image

def ukiyoe_style(image):
    image.filename = "image.png"
    img = Image.open(image)
    img.save("datasets/images/image.png", 'PNG')
    command = "python test.py --dataroot datasets/images --name style_ukiyoe_pretrained --model test --no_dropout --gpu_ids -1"
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")