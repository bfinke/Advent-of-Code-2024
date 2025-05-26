with open("puzzle.txt", "r") as f:
    orders = []
    updates = []
    line = f.readline()
    while line:
        if "|" in line:
            orders.append(line.strip().split("|"))
        elif "," in line:
            updates.append(line.strip().split(","))
        line = f.readline()

middles = 0
for update in updates:
    valid = True
    for num1, num2 in orders:
        if num1 in update and num2 in update:
            if update.index(num1) < update.index(num2):
                continue
            else:
                valid = False
                break
    if valid:
        middles += int(update[len(update) // 2])
print(middles)
