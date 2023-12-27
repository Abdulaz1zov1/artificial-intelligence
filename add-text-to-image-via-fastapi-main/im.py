from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("images.jpeg")
draw = ImageDraw.Draw(img)
draw.text((0, 0),"Sample Text",(255,255,255))
img.save('sample-out.jpg')
