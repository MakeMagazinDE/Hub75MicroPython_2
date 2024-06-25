from pngdec import PNG
from interstate75 import (
     Interstate75, 
     DISPLAY_INTERSTATE75_64X64)

matrix = Interstate75(display = 
         DISPLAY_INTERSTATE75_64X64)

buffer = matrix.display
width = matrix.width
height = matrix.height

png = PNG(buffer)
png.open_file("faces.png")
png.decode(0, 0, source = (8, 0, 8, 8), scale = (3,3))
matrix.update(buffer)