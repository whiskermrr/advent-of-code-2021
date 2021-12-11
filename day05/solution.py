import os
from collections import Counter

def main():
    file = open('input.txt', 'r')

    lines = [line.replace('->', ',').strip().replace(' ', '') for line in file.readlines()]

    solutions(lines)
    

def solutions(lines):
    points, diagonals = [], []

    for line in lines:
        x1, y1, x2, y2 = map(int, line.split(','))
        if x1 == x2:
            points += [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
        elif y1 == y2:
            points += [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
        else:
            if y1 < y2 and x1 < x2:
                diagonals += [(x, y1 + i) for i, x in enumerate(range(x1, x2 + 1))]
            if y1 < y2 and x1 > x2:
                diagonals += [(x, y2 - i) for i, x in enumerate(range(x2, x1 + 1))]
            if y1 > y2 and x1 < x2:
                diagonals += [(x, y1 - i) for i, x in enumerate(range(x1, x2 + 1))]
            if y1 > y2 and x1 > x2:
                diagonals += [(x, y2 + i) for i, x in enumerate(range(x2, x1 + 1))]
                
                

    ### part one
    print(len([point for point, count in Counter(points).items() if count > 1]))
    ### part two
    print(len([point for point, count in Counter(points + diagonals).items() if count > 1]))
    

if __name__ == "__main__":
    main()
