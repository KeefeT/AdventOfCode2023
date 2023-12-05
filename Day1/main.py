
import re

def main():
    file = open("input.txt", "r")

    line = file.readline()
    temp = ""
    sum = 0

    while line:
        matches = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)

        temp += convert(matches[0])
        temp += convert(matches[-1])

        sum += int(temp)

        temp = ""
        line = file.readline()

    print(sum)

    file.close()

def convert(string):
    if string == "one":
        return '1'
    elif string == "two":
        return '2'
    elif string == "three":
        return '3'
    elif string == "four":
        return '4'
    elif string == "five":
        return '5'
    elif string == "six":
        return '6'
    elif string == "seven":
        return '7'
    elif string == "eight":
        return '8'
    elif string == "nine":
        return '9'
    else:
        return string


if __name__ == "__main__":
    main()