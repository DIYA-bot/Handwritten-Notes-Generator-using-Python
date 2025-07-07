from PIL import Image,ImageDraw,ImageFont
import textwrap
text="""Operating System manages hardware resources and provides services for application programs.
They are the backbone of all modern computing system."""

wrap_text=textwrap.fill(text,width=60) #it assure that each line consists of 60 characters
img=Image.new('RGB',(800,600),color='white')
draw=ImageDraw.Draw(img)
font=ImageFont.truetype("handwritten_notes\Burgundia.otf",size=24)
draw.text((40,50),wrap_text,font=font,fill=(0,0,200))
img.save("output.png")
print("Successfully Saved as output.png")

