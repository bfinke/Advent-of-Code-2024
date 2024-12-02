def test_validity(line):
    inc = False
    dec = False
    if line[0] - line[1] < 0:
        inc = True
    else:
        dec = True
    for i in range(1, len(line)):
        if inc and line[i - 1] < line[i] and line[i] - line[i - 1] <= 3:
            continue
        elif dec and line[i - 1] > line[i] and line[i - 1] - line[i] <= 3:
            continue
        else:
            return [False, i]
    return [True, None]


with open("puzzle.txt", "r") as f:
    lines = []
    for i in f:
        line = []
        for v in i.strip().split():
            line.append(int(v))
        lines.append(line)
count = 0
for line in lines:
    validity = test_validity(line)
    if validity[0]:
        count += 1
    # test removing previous value
    elif test_validity(line[:validity[1] - 1] + line[validity[1]:])[0]:
        count += 1
    # test removing current value
    elif test_validity(line[:validity[1]] + line[validity[1] + 1:])[0]:
        count += 1
    # test removing previous previous value (weird edge case)
    elif test_validity(line[:validity[1] - 2] + line[validity[1] - 1:])[0]:
        count += 1
print(count)
