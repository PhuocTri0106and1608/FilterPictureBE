import subprocess
import matplotlib.pyplot as plt
import os

def model(image):
    # uploaded_file_path = "./opt/render/project/src/datasets/images/"+image.filename
    # image.filename = "image.png"
    # uploaded_file_path = "./opt/render/project/src/datasets/images/image.png"
    # image.save(uploaded_file_path)
    command = "python test.py --dataroot ./opt/render/project/src/datasets/images --name style_monet_pretrained --model test --no_dropout --gpu_ids -1"
    try:
        subprocess.run(command, shell=True, check=True)
        style_image_path = "./opt/render/project/src/results/style_monet_pretrained/test_latest/images/image_fake.png"
        print("Command executed successfully.")
        # os.remove(uploaded_file_path)
        return style_image_path
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")