import json

with open("adjacency.json", "r") as json_file:
    data = json.load(json_file)

data["adjacency"] = {}

for row_index, row_node in enumerate(data["nodes"]):
    data["adjacency"][row_node] = {col_node: 0 for col_node in data["nodes"][row_index:]}

if (input("Doing so will overwrite your adjacency matrix, are you sure to proceed? (y/n)").lower() == "y"):
    with open("adjacency.json", "w") as json_file:
        json.dump(data, json_file, indent=4)