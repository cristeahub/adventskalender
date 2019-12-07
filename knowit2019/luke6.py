from PIL import Image

with Image.open('luke6.png') as img:

    pixels = img.load()

    last_pixel = pixels[0,0]

    w, h = img.size

    for i in range(h):
        for j in range(w):
            if (i,j) == (0,0):
                continue

            current_pixel = pixels[j, i]
            pixels[j, i] = (
                current_pixel[0] ^ last_pixel[0],
                current_pixel[1] ^ last_pixel[1],
                current_pixel[2] ^ last_pixel[2]
            )
            last_pixel = current_pixel
    img.show()
