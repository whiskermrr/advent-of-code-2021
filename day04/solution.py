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
    boardsWon = []
    
    winningResult = 0
    lastWinResult = 0
    foundWinner = False

    for line in lines:
        if line == '\n':
            if boardNumbers:
                boards.append(BingoBoard(list(map(lambda number: int(number), boardNumbers)), 5))
            boardNumbers.clear()
        else:
            boardNumbers += line.split()

    boards.append(BingoBoard(list(map(lambda number: int(number), boardNumbers)), 5))

    for i in range(len(numbers)):
        number = numbers[i]
        for j in range(len(boards)):
            board = boards[j]
            board.markNumber(number)
            if board.isWinning() and board not in boardsWon:
                if not foundWinner:
                    winningResult = board.getSumOfUnmarkedNumbers() * number
                    foundWinner = True

                lastWinResult = board.getSumOfUnmarkedNumbers() * number
                boardsWon.append(board)

    print(winningResult)
    print(lastWinResult)


if __name__ == "__main__":
    main()
