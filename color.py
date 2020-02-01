from PIL import Image

image1 = Image.open("image name")
convert_to_bw = image1.convert("L")
convert_to_bw.show()
