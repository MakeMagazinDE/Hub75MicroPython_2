from pngdec import PNG
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

matrix = Interstate75(display = DISPLAY INTERSTATE75_64X64)

buffer = matrix.display
width = matrix.width
height = matrix.height

png = PNG(buffer)
png.open_file("car.png")
png.decode(0, 0)
matrix.update(buffer)