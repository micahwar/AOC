def part1(data):
    count = 0
    for pw in data:
        pw = pw.split(":")
        freq, letter = pw[0].split(" ")
        freq = [int(x) for x in freq.split("-")]
        password = pw[1][1:]
        if password.count(letter) >= freq[0] and password.count(letter) <= freq[1]:
            count += 1
        #print(freq + letter + password)
    return count

def part2(data):
    count = 0
    for pw in data:
        pw = pw.split(":")
        freq, letter = pw[0].split(" ")
        freq = [int(x) for x in freq.split("-")]
        password = pw[1][1:]
        if int(password[freq[0]-1] == letter) + int(password[freq[1]-1] == letter) == 1:
            count += 1
        #print(freq + letter + password)
    return count

def main(inputdata = "input/input2.txt"):
    with open(inputdata, "r") as f:
        data = f.read().split("\n")
    
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()