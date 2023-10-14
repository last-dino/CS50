from PIL import Image
import PIL
import sys
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

in_root, in_ext = os.path.splitext(sys.argv[1].lower())
out_root, out_ext = os.path.splitext(sys.argv[2].lower())

if (in_ext != ".jpg" and in_ext != ".jpeg" and in_ext != ".png") or (out_ext != ".jpg" and out_ext != ".jpeg" and out_ext != ".png"):
    sys.exit("Invalid output")

if in_ext != out_ext:
    sys.exit("Input and output have different extensions")

try:
    before_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

with before_image:
    shirt = Image.open("shirt.png")
    before_image = PIL.ImageOps.fit(before_image, shirt.size)
    before_image.paste(shirt, shirt)
    before_image.save(sys.argv[2])
