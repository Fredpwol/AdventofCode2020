data = open("input.txt", "r")

path = data.readlines()
cleaned_path = [ ln.strip() for ln in path ]
max_window = len(cleaned_path[0])

def find_path_tree(right, down):
    x = 0
    y = 0
    tree_count = 0
    while y < len(cleaned_path):
        if cleaned_path[y][x % max_window] == "#":
            tree_count += 1 
        x += right
        y += down
    return tree_count

directions = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]

res = 1

for dir in directions:
    res *= find_path_tree(dir[0], dir[1])

print(res)