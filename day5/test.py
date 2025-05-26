with open("puzzle.txt", "r") as f:
    orders = {}
    updates = []
    line = f.readline()
    while line:
        if "|" in line:
            num1, num2 = line.strip().split("|")
            if num1 not in orders:
                orders[num1] = [num2]
            else:
                orders[num1].append(num2)
        elif "," in line:
            updates.append(line.strip().split(","))
        line = f.readline()

middles = 0
for update in updates:
    valid = True
    for v in update:
        for num in orders[v]:
            if num not in update:
                continue
            elif update.index(v) < update.index(num):
                continue
            else:
                valid = False
                break
        if not valid:
            break
    if valid:
        middles += int(update[len(update) // 2])
print(middles)
