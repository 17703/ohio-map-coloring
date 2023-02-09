# import some modules for image creation and manipulation
from PIL import Image
from PIL.ImageOps import colorize

# sheck the validity of a state.
def check_validity(state, adjacency):
    for row_node, row in adjacency.items():
        for col_node in row:
            if state[row_node] == state[col_node] and state[row_node] is not None and state[col_node] is not None:
                return False
    return True

def check_validity_quick(state, adjacency, node):
    for adj in adjacency[node]:
        if state[node] == state[adj]:
            return False
    return True

# create the image of the coloring given a state
def create_image(state, colors):
    img = Image.new("RGBA", (1056, 1159), (0, 0, 0))
    for node, color in state.items():
        try:
            overlay = Image.open(f"images/{node}.png").convert("L")
            overlay_colored = colorize(overlay, (0,0,0), colors.get(color, (255, 255, 255)))
            img.paste(overlay_colored, (0, 0), overlay)
        except FileNotFoundError:
            print(f"image \"{node}.png\" not found!")
    return img