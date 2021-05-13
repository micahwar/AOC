def part1(data):
    count = 0
    for vals in data:
        cidIn = False
        valid = True
        for val in vals:
            if val[0] == "cid":
                cidIn = True
        if len(vals) == 8 or (len(vals) == 7 and cidIn==False):
            if valid:
                count += 1
    return count

def part2(data):
    count = 0
    for vals in data:
        cidIn = False
        valid = True
        for val in vals:
            if val[0] == "byr":
                if (len(val[1]) != 4 or int(val[1]) < 1920 or int(val[1]) > 2002):
                    valid = False
            elif val[0] == "iyr":
                if (len(val[1]) != 4 or int(val[1]) < 2010 or int(val[1]) > 2020):
                    valid = False
            elif val[0] == "eyr":
                if (len(val[1]) != 4 or int(val[1]) < 2020 or int(val[1]) > 2030):
                    valid = False
            elif val[0] == "hgt":
                if val[1][-2:] == "cm":
                    #print()
                    if int(val[1][:-2]) <150 or int(val[1][:-2]) > 193:
                        valid = False
                elif val[1][-2:] == "in":
                    if int(val[1][:-2]) <59 or int(val[1][:-2]) > 76:
                        valid = False
                else:
                    valid = False
            elif val[0] == "hcl":
                if (len(val[1]) != 7 or val[1][0] != '#'):
                    try:
                        int(val[1][1:])
                    except ValueError:
                        valid = False
            elif val[0] == "ecl":
                if val[1] != 'amb' and  val[1] != 'blu' and  val[1] != 'brn' and  val[1] != 'gry' and  val[1] != 'grn' and  val[1] != 'hzl' and val[1] != 'oth':
                    valid = False
            elif val[0] == "pid":
                if len(val[1]) != 9 or not val[1].isnumeric():
                    valid = False
            elif val[0] == "cid":
                cidIn = True
        if len(vals) == 8 or (len(vals) == 7 and cidIn==False):
            if valid:
                count += 1
    return count


def main(inputdata = "input/input4.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n\n")
    xdata = []
    for line in data:
        vals = []
        for x in line.split("\n"):
            for y in x.split(" "):
                vals.append(y)
        xdata.append([x.split(":") for x in vals])
    print(part1(xdata))
    print(part2(xdata))


if __name__ == "__main__":
    main()