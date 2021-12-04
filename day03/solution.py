import os

def main():
    file = open('input.txt', 'r')
    numbers = [line.strip() for line in file.readlines()]
    partOne(numbers)
    partTwo(numbers)        

def partOne(numbers):
    noOfNoises = len(numbers)
    noOfBits = len(numbers[0])

    gammaRate = int(''.join([str(int(sum([int(bit) for bit in [x for y in numbers for x in y]][i::noOfBits]) >= noOfNoises / 2)) for i in range(0, noOfBits)]), 2)
    epsilonRate = pow(2, noOfBits) - gammaRate - 1
        
    print(gammaRate * epsilonRate)

def partTwo(numbers):
    oxygenNumbers = numbers.copy()
    co2Numbers = numbers.copy()

    print(calculateRating(oxygenNumbers, '1', '0') * calculateRating(co2Numbers, '0', '1'))

def calculateRating(numbers, trueStatement, falseStatement):
    noOfBits = len(numbers[0])
    
    for i in range(0, noOfBits):
        noOfNoises = len(numbers)
        if noOfNoises == 1: break
        totalOnes = sum([int(bit) for bit in [x for y in numbers for x in y]][i::noOfBits])
        numbers = list(filter(lambda number: number[i] == (trueStatement if (totalOnes >= noOfNoises / 2) else falseStatement), numbers))

    return int(numbers[0], 2)

if __name__ == "__main__":
    main()
