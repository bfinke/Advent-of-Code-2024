def xmas_finder(x, m, a, s):
    if x == "X" and m == "M" and a == "A" and s == "S":
        return True
    return False


with open("puzzle.txt", "r") as f:
    lines = [i.strip() for i in f]

count = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        # up
        if y >= 3 and xmas_finder(lines[y][x], lines[y - 1][x], lines[y - 2][x], lines[y - 3][x]):
            count += 1
        # down
        if len(lines) - y >= 4 and xmas_finder(lines[y][x], lines[y + 1][x], lines[y + 2][x], lines[y + 3][x]):
            count += 1
        # right
        if len(lines[0]) - x >= 4 and xmas_finder(lines[y][x], lines[y][x + 1], lines[y][x + 2], lines[y][x + 3]):
            count += 1
        # left
        if (x >= 3) and xmas_finder(lines[y][x], lines[y][x - 1], lines[y][x - 2], lines[y][x - 3]):
            count += 1
        # top_left
        if x >= 3 and y >= 3 and xmas_finder(lines[y][x], lines[y - 1][x - 1], lines[y - 2][x - 2], lines[y - 3][x - 3]):
            count += 1
        # top_right
        if len(lines[0]) - x >= 4 and y >= 3 and xmas_finder(lines[y][x], lines[y - 1][x + 1], lines[y - 2][x + 2], lines[y - 3][x + 3]):
            count += 1
        # bottom_right
        if len(lines[0]) - x >= 4 and len(lines) - y >= 4 and xmas_finder(lines[y][x], lines[y + 1][x + 1], lines[y + 2][x + 2], lines[y + 3][x + 3]):
            count += 1
        # bottom_left
        if x >= 3 and len(lines) - y >= 4 and xmas_finder(lines[y][x], lines[y + 1][x - 1], lines[y + 2][x - 2], lines[y + 3][x - 3]):
            count += 1
print(count)
