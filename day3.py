"""
Task:
To analyse the toboggan route for trees
"""


def create_map(filename: str):
    map = []
    with open(filename, 'r') as infile:
        for line in infile:
            map.append(line.strip("\n"))
    return map


def count_trees_in_path(map: list, horizontal: int, vertical: int):
    tree_count = 0
    position = 0
    for row, landscape in enumerate(map):
        if row % vertical != 0:
            continue
        elif vertical == 1:
            if landscape[(row * horizontal) % len(landscape)] == "#":
                tree_count += 1
        else:
            if landscape[position % len(landscape)] == "#":
                tree_count += 1
            position += horizontal
    return tree_count

    
map_list = create_map("day3_toboggan_map.txt")
trees = count_trees_in_path(map_list, 3, 1)
print(f"There are {trees} trees in Santa's toboggan path")
# Should be 274
"""
Alternative routes to look at: 

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

"""
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]

total_trees = 1

for i in range(0, len(right)):
    trees = count_trees_in_path(map_list, right[i], down[i])
    print(f"Right {right[i]}, down {down[i]}: "
          f"There are {trees} trees in Santa's toboggan path")
    total_trees = trees * total_trees

print(f"Total trees hit: {total_trees}")

#6050183040 is correct answer
