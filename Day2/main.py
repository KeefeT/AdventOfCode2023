
import re

def main():
    file = open("input.txt", "r")
    sum = 0
    line = file.readline()
    # part one 
    # impossible = []
    # flag = True

    while line:
        rounds = line.split(';')

        red = 0 
        blue = 0 
        green = 0 

        for round in rounds:
            matches = re.findall(r"(\d*) (green|blue|red)", round)
            # part one
            # for match in matches:
            #     if match[1] == 'red' and int(match[0]) > 12:
            #         flag = False
            #     elif match[1] == 'green' and int(match[0]) > 13:
            #         flag = False
            #     elif match[1] == 'blue' and int(match[0]) > 14:
            #         flag = False

            # part two
            for match in matches:
                if match[1] == 'red' and int(match[0]) > red:
                    red = int(match[0])
                elif match[1] == 'green' and int(match[0]) > green:
                    green = int(match[0])
                elif match[1] == 'blue' and int(match[0]) > blue:
                    blue = int(match[0])

        # part one
        # impossible.append(flag)
        # flag = True

        power = red * green * blue
        sum += power

        line = file.readline()
        
    # part one
    # count = 1
    # for id in impossible:
    #     if id:
    #         sum += count
    #     count += 1

    print(sum)

    file.close()

if __name__ == '__main__':
    main()