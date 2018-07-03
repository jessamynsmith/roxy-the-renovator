import os
from PIL import Image


input_dir = "/Users/jessamyn/Google Drive/roxanne/Website Photos"
output_dir = "/Users/jessamyn/Downloads/Website Photos - resized"

max_width = 960
max_height = 720


for root, dirs, files in os.walk(input_dir):
    if not files:
        for dir_name in dirs:
            try:
                os.mkdir(os.path.join(output_dir, dir_name))
            except FileExistsError:
                pass
    for file in files:
        try:
            img = Image.open(os.path.join(root, file))
        except OSError:
            continue
        ratio = 1.0 * img.width / max_width
        img = img.resize((max_width, int(round(img.height/ratio))), Image.ANTIALIAS)
        img.save(os.path.join(output_dir, os.path.split(root)[-1], file))
