data = open("input.txt", "r")

def parse_line(unprocessed_data):
    policy, password = unprocessed_data.strip().split(": ")
    min, max = policy[:-1].strip().split("-")

    return {"min": int(min), "max": int(max), "char": policy[-1], "password": password}


def is_valid(password_data):
    char_count = 0
    for char in password_data["password"]:
        if char == password_data["char"]:
            char_count += 1
    return password_data["min"] <= char_count <= password_data["max"]

count = 0 
for value in data.readlines():
    if is_valid(parse_line(value)):
        count += 1 

print(count)
