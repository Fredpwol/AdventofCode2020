data = open("input.txt", "r")

path = data.readlines()
cleaned_path = [ ln.strip() for ln in path ]
max_window = len(cleaned_path[0])

x = 0
y = 0
tree_count = 0
while y < len(cleaned_path):
    if cleaned_path[y][x % max_window] == "#":
        tree_count += 1 
    x += 3
    y += 1

print(tree_count)