import subprocess
import matplotlib.pyplot as plt
import os

def model(image):
    uploaded_file_path = "./opt/render/project/src/datasets/images/"+image.filename
    image.save(uploaded_file_path)
    command = "python test.py --dataroot ./opt/render/project/src/datasets/images --name style_monet_pretrained --model test --no_dropout --gpu_ids -1"
    try:
        subprocess.run(command, shell=True, check=True)
        filename_fake = image.filename[:-4] + "_fake.png" 
        style_image_path = "./opt/render/project/src/results/style_monet_pretrained/test_latest/images/" + filename_fake
        style_image = plt.imread(style_image_path)
        print("Command executed successfully.")
        # os.remove(uploaded_file_path)
        return style_image
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")