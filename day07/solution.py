import os

def main():
    positions = list(map(int, open('input.txt', 'r').readline().strip().split(',')))
    partOne(positions)
    partTwo(positions)

def partOne(positions):
    positions.sort()
    dest = positions[len(positions) // 2]
    fuel = 0

    for pos in positions:
        fuel = fuel + abs(pos - dest)

    print(fuel)

def partTwo(positions):
    dest = sum(positions) // len(positions)
    fuel = 0

    for pos in positions:
        move = abs(pos - dest)
        fuel = fuel + round((move / 2) * (move + 1))

    print(fuel)


if __name__ == "__main__":
    main()
