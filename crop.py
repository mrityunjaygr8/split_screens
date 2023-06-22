from PIL import Image, ImageDraw

BLACK_IMAGE = "black.png"
WHITE_IMAGE = "while.png"

whiteImg = Image.open(WHITE_IMAGE)
blackImg = Image.open(BLACK_IMAGE)
w, h = whiteImg.size
mask = Image.new("L", whiteImg.size, 0)
draw = ImageDraw.Draw(mask)
#This is named option-1
# draw.polygon([(0, 0), (w*0.6, 0), (w*0.4, h), (0, h)], fill=255)
#This is named option-2
# draw.polygon([(0, h), (w, h), (w*0.5, 0)], fill=255)
# This is option-3
draw.polygon([(0, 0), (w, 0), (0, h)], fill=255)
im = Image.composite(whiteImg, blackImg, mask)
im.save("option-3.png")
