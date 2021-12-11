import os
from collections import Counter

def main():
    file = open('input.txt', 'r')

    lines = [line.replace('->', ',').strip().replace(' ', '') for line in file.readlines()]

    points = []

    for line in lines:
        x1, y1, x2, y2 = map(int, line.split(','))
        if x1 == x2:
            points += [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
        if y1 == y2:
            points += [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]

    print(len([point for point, count in Counter(points).items() if count > 1]))
    

if __name__ == "__main__":
    main()
