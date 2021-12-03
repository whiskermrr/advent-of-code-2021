import os
import more_itertools as itertools

def main():
    depths = list(map(int, open('input.txt', 'r').readlines()))

    partOne(depths)
    partTwo(depths)

def partOne(depths):
    increasedCount = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increasedCount += 1

    print(increasedCount)

def partTwo(depths):
    partOne([sum(window) for window in list(itertools.windowed(depths, n = 3, step = 1))])

if __name__ == "__main__":
    main()
