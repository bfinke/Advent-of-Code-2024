with open("puzzle.txt", "r") as f:
    lines = []
    for i in f:
        line = []
        for v in i.strip().split():
            line.append(int(v))
        lines.append(line)
count = 0
for line in lines:
    inc = False
    dec = False
    if line[0] - line[1] < 0:
        inc = True
    else:
        dec = True

    valid = True
    for i in range(1, len(line)):
        if inc and line[i - 1] < line[i] and line[i] - line[i - 1] <= 3:
            continue
        elif dec and line[i - 1] > line[i] and line[i - 1] - line[i] <= 3:
            continue
        else:
            valid = False
            break
    count += valid
print(count)
