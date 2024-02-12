def is_at_origin(string):
    horizontal = 0
    vertical = 0
    
    for letter in string:
        if letter == "L":
            horizontal -= 1
        elif letter == "R":
            horizontal += 1
        elif letter == "U":
            vertical += 1
        elif letter == "D":
            vertical -= 1

    return horizontal == 0 and vertical == 0

inputs = ["LR", "URURD", "RUULLDRD"]

for input in inputs:
    print(is_at_origin(input))
