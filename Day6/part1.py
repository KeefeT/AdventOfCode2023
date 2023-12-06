

import re

def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    arr = []

    times = re.findall(r'\d+', lines[0])
    distances = re.findall(r'\d+', lines[1])

    print(times)
    print(distances)

    for x in range(0, len(times)):
        time = int(times[x])
        record = int(distances[x])
        wins = 0

        for t in range(0, time):
            v = t
            time_remaining = int(times[x]) - t
            d = distance(v, time_remaining)
            if d > record:
                wins += 1

        if wins != 0:
            arr.append(wins)
            wins = 0

    product = 1
        
    for num in arr:
        product *= num

    print(product)
    file.close()

def distance(v: int, t: int):
    return v * t


if __name__ == '__main__':
    main()