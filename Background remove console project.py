from PIL import Image
from rembg import remove

input_img="j_img.jpg"
input_img_open=Image.open(input_img)
output_image=remove(input_img_open)

output_image.save("output_img.png")

print("Background has been removed and process completed....")