from typing import Text
from PIL import Image,ImageFont,ImageDraw
img = Image.open("Question.png")
Result1 = Image.open('AskImagify.png')
draw=ImageDraw.Draw(img)
font = ImageFont.truetype("Font.ttf",12)
# use \n for next line

Text = "Chintu has 4 apples, \nRamesh' train is 7 minutes early.\nWhat is the mass of the sun?"

# use the below coordinates to align your question
draw.text((35,75),Text,(0,0,0),font=font)
Result = img.save("AskImagify.png")
Result1.show()