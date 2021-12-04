import os

def main():
    commands = [[command[0], int(command[1])] for command in [line.split() for line in open('input.txt', 'r').readlines()]]

    partOne(commands)
    partTwo(commands)
    

def partOne(commands):
    horizontalPos = 0
    depth = 0

    for command in commands:
        direction = command[0]
        value = command[1]
        
        if direction == 'forward': horizontalPos += value
        elif direction == 'up': depth -= value
        elif direction == 'down': depth += value

    print(depth * horizontalPos)


def partTwo(commands):
    horizontalPos = 0
    depth = 0
    aim = 0

    for command in commands:
        direction = command[0]
        value = command[1]
        
        if direction == 'forward':
            horizontalPos += value
            depth += (aim * value)
        elif direction == 'up': aim -= value
        elif direction == 'down': aim += value


    print(depth * horizontalPos)
        
if __name__ == "__main__":
    main()
