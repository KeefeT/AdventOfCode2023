
import re

def main():
    file = open("input.txt", "r")
    line = file.readline()
    total = 0

    while line:

        line = line.split('|')
        line[0] = line[0].split(':')[1]

        winning = re.findall(r'(\d+)', line[0])
        numbers = re.findall(r'(\d+)', line[1])

        print(f'winning:{winning}, numbers:{numbers}')

        line = file.readline()

        points = 0

        for num in numbers:
            if num in winning:
                if points == 0:
                    points += 1
                else:
                    points *= 2

        total += points





    print(total)
    file.close()


if __name__ == '__main__':
    main()
