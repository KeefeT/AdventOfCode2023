

import re

def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    arr = []

    times = re.findall(r'\d+', lines[0])
    distances = re.findall(r'\d+', lines[1])

    time = ''
    distance = ''
    for num in times:
        time += num
    for dis in distances:
        distance += dis

    time = int(time)
    record = int(distance)
    wins = 0

    for t in range(0, time):
        v = t
        time_remaining = time - t
        d = drt(v, time_remaining)
        if d > record:
            wins += 1

    print(wins)
    file.close()

def drt(v: int, t: int) -> int:
    return v * t


if __name__ == '__main__':
    main()