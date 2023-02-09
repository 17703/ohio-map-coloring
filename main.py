# import some modules for JSON operations and utilities
import json
from util import create_image, check_validity_quick

# define the colors of the nodes
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0)
    #"blue": (0, 64, 255)
}

# open the verbose adjacency file and load it into a variable
with open("verbose.json", "r") as json_file:
    verbose = json.load(json_file)

# node names and colors
nodes = {node: None for node in verbose.keys()}
node_names = list(nodes.keys())

flag = 1

# color states recursively with backtracking
def color_states(node_index=0):
    # initialize some variables to reduce code reuse
    node_name = node_names[node_index]
    last_node = node_index == len(nodes) - 1

    # try every defined color
    for c in colors.keys():
        # try to color the current node the current color
        nodes[node_name] = c

        #img = create_image(nodes, colors)
        #img.show()

        # if we are still in a valid state after that
        if check_validity_quick(nodes, verbose, node_name):

            # return True if we are on the last node or if we could successfully color the subsequent nodes
            if last_node or color_states(node_index+1):
                return True

    # if we have tried every color and still not returned True, it is impossible to be valid given the previous state
    else:
        global flag
        if flag:
            flag = 0
            img = create_image(nodes, colors)
            img.save("conflict.png")
            img.show()

        # undo current node's color and return false
        nodes[node_name] = None
        return False

# color the states and print out the final configuration
if color_states():
    print(json.dumps(nodes, indent=4))

    # Create the image of the state, save it, and show it
    img = create_image(nodes, colors)
    img.save("output.png")
    img.show()
else:
    print("Could not find a valid state")