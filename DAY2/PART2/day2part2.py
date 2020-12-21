data = open("input.txt", "r")

def parse_line(unprocessed_data):
    policy, password = unprocessed_data.strip().split(": ")
    min, max = policy[:-1].strip().split("-")

    return {"min": int(min), "max": int(max), "char": policy[-1], "password": password}


def is_valid(password_data):
    return (password_data["password"][password_data["min"]-1] == password_data["char"] or 
    password_data["password"][password_data["max"]-1] == password_data["char"] )and (not ( 
    password_data["password"][password_data["min"]-1] == password_data["char"] and 
    password_data["password"][password_data["max"]-1] == password_data["char"]))

count = 0 
for value in data.readlines():
    if is_valid(parse_line(value)):
        count += 1 

print(count)
