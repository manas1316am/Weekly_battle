# stepic is the a py module for CLI tool for hiding data inside the png image.
from PIL import Image
import stepic

# Open the image first
first = Image.open('coder.png')
# Encode the data that you wanted to save
first = stepic.encode(first, b'Hello there!')
# save the changed image
first.save('coder.png')
# open the new image
""" 
	You will not find any difference in both the images (old and changed).
"""
first = Image.open('coder.png')
first.show()
# Decode the image
dec = stepic.decode(first)
#print the hidden data
print (dec)
