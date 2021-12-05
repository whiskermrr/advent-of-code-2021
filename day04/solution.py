import os

class BingoBoard:
    def __init__(self, numbers, size):
        self.fields = list(map(BingoField, numbers))
        self.size = size

    def markNumber(self, number):
        for field in self.fields:
            if field.number == number:
                field.mark()

    def isWinning(self):
        for i in range(0, self.size):
            if all(list(map(lambda field: field.marked, self.fields[i * self.size: i * self.size + self.size]))):
                return True

            if all(list(map(lambda field: field.marked, self.fields[i::self.size]))):
                return True
        
        return False

    def getSumOfUnmarkedNumbers(self):
        return sum(list(map(lambda field: field.number, list(filter(lambda field: field.marked == False, self.fields)))))

class BingoField:
    def __init__(self, number):
        self.number = number
        self.marked = False

    def mark(self):
        self.marked = True

def main():
    file = open('input.txt', 'r')
    numbers = list(map(lambda number: int(number), file.readline().strip().split(',')))
    lines = file.readlines()

    boards = []
    boardNumbers = []

    for line in lines:
        if line == '\n':
            if boardNumbers:
                boards.append(BingoBoard(list(map(lambda number: int(number), boardNumbers)), 5))
            boardNumbers.clear()
        else:
            boardNumbers += line.split()

    winningResult = 0
    foundWinner = False

    for number in numbers:
        for board in boards:
            board.markNumber(number)
            if board.isWinning():
                winningResult = board.getSumOfUnmarkedNumbers() * number
                foundWinner = True
                break
        if foundWinner: break

    print(winningResult)


if __name__ == "__main__":
    main()
