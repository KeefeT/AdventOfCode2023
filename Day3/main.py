
def main():
    file = open("input.txt", "r")
    line = file.readline()
    sum = 0
    # array of strings
    arr = []

    while line:
        arr.append(line)
        line = file.readline()

    nums = check_adjacent(arr)
    
    for num in nums:
        sum += num

    print(sum)

    file.close()


def check_adjacent(arr):
    
    nums_to_sum = []
    num = ''
    inNum = False
    isTouching = False
    touched = False

    for y in range(0, len(arr)):
        for x in range(0, len(arr[-1])):
            # print(f'{x},{y} {arr[y][x]}')

            inNum = (arr[y][x].isdigit())
            isTouching = calculateTouching(x, y, arr)
                    
            if inNum:
                if isTouching:
                    touched = True
                num += arr[y][x]
                isTouching = False
            elif num != '':
                if touched:
                    nums_to_sum.append(int(num))
                num = ''
                touched = False

        if num !=  '':
            if touched:
                nums_to_sum.append(int(num))
            num = ''

        touched = False
        isTouching = False

    return nums_to_sum



def calculateTouching(x, y, arr):
    isTouching = False

    try:
        isTouching = (arr[y-1][x].isdigit() == False and arr[y-1][x] != '.' and arr[y-1][x] != '\n')
    except:
        None

    if isTouching:
        return isTouching

    try:
        isTouching = (arr[y-1][x-1].isdigit() == False and arr[y-1][x-1] != '.' and arr[y-1][x-1] != '\n')
    except:
        None

    if isTouching:
        return isTouching

    try:
        isTouching = (arr[y-1][x+1].isdigit() == False and arr[y-1][x+1] != '.' and arr[y-1][x+1] != '\n')
    except:
        None

    if isTouching:
        return isTouching

    try:
        isTouching = (arr[y+1][x].isdigit() == False and arr[y+1][x] != '.' and arr[y+1][x] != '\n')
    except:
        None

    if isTouching:
        return isTouching

    try:
        isTouching = (arr[y+1][x-1].isdigit() == False and arr[y+1][x-1] != '.' and arr[y+1][x-1] != '\n')
    except:
        None

    if isTouching:
        return isTouching

    try:
        isTouching = (arr[y+1][x+1].isdigit() == False and arr[y+1][x+1] != '.' and arr[y+1][x+1] != '\n')
    except:
        None

    if isTouching:
        return isTouching

    try:
        isTouching = (arr[y][x+1].isdigit() == False and arr[y][x+1] != '.' and arr[y][x+1] != '\n')
    except:
        None

    if isTouching:
        return isTouching

    try:
        isTouching = (arr[y][x-1].isdigit() == False and arr[y][x-1] != '.' and arr[y][x-1] != '\n')
    except:
        None

    return isTouching

if __name__ == '__main__':
    main()