
data = open("input.txt", "r")
inputs = [ int(ln) for ln in data.readlines() ]
inputs.sort()


total = 2020
def solve(values):
    ptr1 = 0
    ptr2 = len(values)-1
    while ptr1 < ptr2:
        if (values[ptr1] + values[ptr2] < total):
            ptr1 += 1
        elif (values[ptr1] + values[ptr2] > total):
            ptr2 -= 1
        else:
            return values[ptr1] * values[ptr2]

print(solve(inputs))
