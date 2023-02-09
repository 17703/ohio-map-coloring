from PIL import Image
from PIL.ImageOps import colorize

ashland = Image.open("ashland.png").convert("L")
richland = Image.open("richland.png").convert("L")
wayne = Image.open("wayne.png").convert("L")

ashland_colored = colorize(ashland, (0, 0, 0), (255, 0, 0))
richland_colored = colorize(richland, (0, 0, 0), (0, 255, 0))
wayne_colored = colorize(wayne, (0, 0, 0), (0, 0, 255))

size = ashland.size
print(size)

img = Image.new("RGBA", size, (0, 0, 0, 0))

img.paste(ashland_colored, (0, 0), ashland)
img.paste(richland_colored, (0, 0), richland)
img.paste(wayne_colored, (0, 0), wayne)

img.show()