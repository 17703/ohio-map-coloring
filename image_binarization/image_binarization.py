from PIL import Image

# https://mapsofusa.net/ohio-map-with-cities-and-towns/
ohio = Image.open("ohio_map_original.png").convert("L")
#ohio.show()

# image binarization
threshold = 150
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
#ohio_converted = ohio.point(table, '1')

#ohio_converted = ohio.point(lambda i: i > threshold, '1')
ohio_converted = ohio.point(lambda i: i > threshold and 255)
ohio_converted.save("China_map_converted.png")
ohio_converted.show()