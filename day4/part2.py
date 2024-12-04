def xmas_finder(m, a, s):
    if m == "M" and a == "A" and s == "S":
        return True
    return False


with open("puzzle.txt", "r") as f:
    lines = [i.strip() for i in f]

count = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "A" and y >= 1 and x >= 1 and len(lines) - y >= 2 and len(lines[0]) - x >= 2:
            top_left_to_bottom_right = xmas_finder(lines[y - 1][x - 1], lines[y][x], lines[y + 1][x + 1])
            bottom_right_to_top_left = xmas_finder(lines[y + 1][x + 1], lines[y][x], lines[y - 1][x - 1])
            top_right_to_bottom_left = xmas_finder(lines[y - 1][x + 1], lines[y][x], lines[y + 1][x - 1])
            bottom_left_to_top_right = xmas_finder(lines[y + 1][x - 1], lines[y][x], lines[y - 1][x + 1])
            if (top_left_to_bottom_right or bottom_right_to_top_left) and (top_right_to_bottom_left or bottom_left_to_top_right):
                count += 1
print(count)
