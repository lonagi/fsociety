import os
from PIL import Image

path = "imgs/"
pdf_filename = "./result.pdf"
im_list = []

for file in os.listdir(path=path):
    if file.split(".")[-1] in ("jpg","png","svg","jpeg","gif"):
        im_list.append(Image.open(path+file).convert("RGB"))

im_list[0].save(pdf_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list[1:])