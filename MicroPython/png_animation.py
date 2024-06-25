from pngdec import PNG
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

#Displayobjekt und Buffer
matrix = Interstate75(display = DISPLAY_INTERSTATE75_64X64)
buffer = matrix.display

#Displaygröße
width = matrix.width
height = matrix.height

png = PNG(buffer)

for image in range(36):
    png.open_file("/animation/" + str(image) + ".png")
    png.decode(0, 0)
    image += 1
    matrix.update(buffer)
