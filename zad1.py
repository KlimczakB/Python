#!/usr/bin/python3

from PIL import Image

im = Image.open('dog.jpg')

print(im.mode)
print(im.size)
print(im.width)
print(im.height)
print(im.format)

im.show()
