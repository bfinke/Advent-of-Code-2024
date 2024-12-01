with open("puzzle.txt", "r") as f:
    left = []
    right = []
    for line in f:
        l, r = line.strip().split()
        left.append(int(l))
        right.append(int(r))
left.sort()
right.sort()
total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])
print(total)
