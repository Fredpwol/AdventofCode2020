data = open("input.txt", "r")
inputs = [ int(ln) for ln in data.readlines() ]
inputs.sort()

total = 2020
def solve(values):
    for i in range(len(values)):
        curr_value = values[i]
        ptr1 = 0
        ptr2 = len(values)-1
        while ptr1 < ptr2:
            if ptr1 == curr_value:
                ptr1 += 1
                continue
            if ptr2 == curr_value:
                ptr2 -= 1
                continue

            if (curr_value + values[ptr1] + values[ptr2] < total):
                ptr1 += 1
            elif (curr_value + values[ptr1] + values[ptr2] > total):
                ptr2 -= 1
            else:
                return values[ptr1] * values[ptr2] * curr_value

print(solve(inputs))