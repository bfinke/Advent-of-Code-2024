import string

with open("example2.txt", "r") as f:
    line = f.read()

line1 = line
do_lst = [0]
dont_lst = []
pos = 0
while pos < len(line1):
    do = line1.find("do()")
    dont = line1.find("don't()")
    if (do < dont and do != -1) or (do != -1 and dont == -1):
        do_lst.append(do)
        line1 = line1[do + 4:]
        pos = do + 4
    elif (dont < do and dont != -1) or (dont != -1 and do == -1):
        dont_lst.append(dont)
        line1 = line1[dont + 7:]
        pos = dont + 7
    else:
        break

digits = string.digits
total = 0
curr_do = 0
curr_dont = dont_lst[0]
while line.find("mul") != -1:
    mul = line.find("mul")
    if (mul > curr_do and mul < curr_dont) or (mul < curr_do and mul > curr_dont):
        pass
    elif
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
