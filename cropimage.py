from PIL import Image

left = int(input("Pixels From Left : "))
top = int(input("Pixels From Top : "))
right = int(input("Pixels From Right : "))
bottom = int(input("Pixels From Bottom : "))
img_path = str(input("enter Image path : "))

image1 = Image.open(img_path)
crop_image = image1.crop((left, top, right, bottom))


crop_image.show()