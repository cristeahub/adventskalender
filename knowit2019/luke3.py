from PIL import Image


with open('world.txt') as f:
    b = list(map(int, list(f.read().strip())))

w = 1287

img = Image.new('RGB', (w, w))
img.putdata([(255*b[x], 255*b[x], 255*b[x]) for x in range(len(b))])

img.show()
