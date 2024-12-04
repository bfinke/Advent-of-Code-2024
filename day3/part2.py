import string

with open("puzzle.txt", "r") as f:
    line = f.read()

do_lst = [0]
dont_lst = []
while True:
    do = line.find("do()")
    dont = line.find("don't()")
    if do == -1 and dont == -1:
        break
    elif ((do < dont and do != -1) or dont == -1):
        do_lst.append(do)
        line = line[:do] + "...." + line[do + 4:]
    elif ((dont < do and dont != -1) or do == -1):
        dont_lst.append(dont)
        line = line[:dont] + "......." + line[dont + 7:]
    else:
        break

digits = string.digits
total = 0
begin_do = 0
begin_dont = 0
while line.find("mul") != -1:
    mul = line.find("mul")
    for i in do_lst:
        if mul - i > 0:
            begin_do = i
    for i in dont_lst:
        if mul - i > 0:
            begin_dont = i
    if begin_do < begin_dont:
        line = line[:mul] + "..." + line[mul + 3:]
        continue
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
                line = line[:mul] + "..." + line[mul + 3:]
                continue
            else:
                line = line[:mul] + "..." + line[mul + 3:]
                continue
        else:
            line = line[:mul] + "..." + line[mul + 3:]
            continue
    else:
        line = line[:mul] + "..." + line[mul + 3:]
        continue
print(total)
