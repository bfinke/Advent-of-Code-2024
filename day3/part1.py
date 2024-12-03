import string

with open("puzzle.txt", "r") as f:
    line = f.read()

digits = string.digits
total = 0
while line.find("mul") != -1:
    mul = line.find("mul")
    num1 = ""
    num2 = ""
    comma = ""
    comma_found = False
    back_par = ""
    back_par_found = False
    if line[mul + 3] == "(":
        for i, v in enumerate(line[mul + 4:mul + 8]):
            if v in digits:
                num1 += v
            elif v == ",":
                comma = mul + 4 + i
                comma_found = True
                break
            else:
                break
        if comma_found:
            for i, v in enumerate(line[comma + 1:comma + 5]):
                if v in digits:
                    num2 += v
                elif v == ")":
                    back_par = comma + 1 + i
                    back_par_found = True
                else:
                    break
            if back_par_found:
                total += int(num1) * int(num2)
                line = line[back_par:]
                continue
            else:
                line = line[comma:]
                continue
        else:
            line = line[mul + 3:]
            continue
    else:
        line = line[mul + 3:]
        continue
print(total)
