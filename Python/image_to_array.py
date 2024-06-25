from PIL import Image

width = 36
height = 36

image_path = 'sonnig_wolken_36x36.jpg'
image = Image.open(image_path)

image = image.convert('L')

array = []
for y in range(height):
    row = []
    for x in range(width):
        pixel = image.getpixel((x,y))
        if pixel < 64:
            value = 0
        elif pixel < 128:
            value = 1
        elif pixel < 192:
            value = 2
        else:
            value = 3
        row.append(value)
    array.append(row)
        
for row in array:
    print(','.join(map(str, row)) + ',')