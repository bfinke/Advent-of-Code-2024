with open("puzzle.txt", "r") as f:
    left = []
    right = []
    for line in f:
        l, r = line.strip().split()
        left.append(int(l))
        right.append(int(r))
total = 0
for i in left:
    total += i * right.count(i)
print(total)
