import os

def main():
    lines = open('input.txt', 'r').readlines()
    partOne(lines)
    partTwo(lines)

def partOne(lines):
    outputs = [output.split() for output in [line.strip().split('|')[1] for line in lines]]
    sizes = [2, 4, 3, 7]
    values = [value for output in outputs for value in output]

    noOfAppearance = 0
    
    for value in values:
        if len(value) in sizes:
            noOfAppearance = noOfAppearance + 1

    print(noOfAppearance)

def partTwo(lines):
    numbersPart = [line.strip().split('|')[0] for line in lines]
    outputsPart = [line.strip().split('|')[1] for line in lines]

    zeroSegments = [0, 1, 2, 4, 5, 6]
    twoSegments = [0, 2, 3, 4, 6]
    threeSegments = [0, 2, 3, 5, 6]
    fiveSegments = [0, 1, 3, 5, 6]
    sixSegments = [0, 1, 3, 4, 5, 6]
    nineSegments = [0, 1, 2, 3, 5, 6]

    sumOfoutputs = 0
    

    for i, numberPart in enumerate(numbersPart):
        segments = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}
        numbers = numberPart.split()

        sixSegmentsNumbers = getNumbers(numbers, 6)
        fiveSegmentsNumbers = getNumbers(numbers, 5)
        
        one = getNumbers(numbers, 2)[0]
        seven = getNumbers(numbers, 3)[0]
        four = getNumbers(numbers, 4)[0]
        eight = getNumbers(numbers, 7)[0]
        
        six = [number for i, number in enumerate(sixSegmentsNumbers) if not all(j in number for j in one)][0]
        sixSegmentsNumbers.remove(six)
        
        segments[0] = [segment for segment in seven if segment not in one][0]
        segments[2] = [segment for segment in eight if segment not in six][0]

        five = [number for i, number in enumerate(fiveSegmentsNumbers) if not segments[2] in number][0]
        fiveSegmentsNumbers.remove(five)
        
        segments[4] = [segment for segment in six if segment not in five][0]

        nine = [number for i, number in enumerate(sixSegmentsNumbers) if not segments[4] in number][0]
        sixSegmentsNumbers.remove(nine)

        zero = sixSegmentsNumbers[0]

        three = [number for i, number in enumerate(fiveSegmentsNumbers) if not segments[4] in number][0]
        fiveSegmentsNumbers.remove(three)

        two = fiveSegmentsNumbers[0]

        segments[3] = [segment for segment in eight if segment not in zero][0]
        segments[1] = [segment for segment in eight if segment not in three and segment not in segments.values()][0]
        segments[5] = [segment for segment in eight if segment not in two and segment not in segments.values()][0]
        segments[6] = [segment for segment in eight if segment not in segments.values()][0]

        finalOutput = ''

        for output in outputsPart[i].split():
            outputLength = len(output)
            if outputLength == 2:
                finalOutput = finalOutput + '1'
            elif outputLength == 3:
                finalOutput = finalOutput + '7'
            elif outputLength == 4:
                finalOutput = finalOutput + '4'
            elif outputLength == 7:
                finalOutput = finalOutput + '8'
            else:
                outputSegments = [list(segments.keys())[list(segments.values()).index(segment)] for segment in output]
                outputSegments.sort()
                if set(outputSegments) == set(zeroSegments):
                    finalOutput = finalOutput + '0'
                elif set(outputSegments) == set(twoSegments):
                    finalOutput = finalOutput + '2'
                elif set(outputSegments) == set(threeSegments):
                    finalOutput = finalOutput + '3'
                elif set(outputSegments) == set(fiveSegments):
                    finalOutput = finalOutput + '5'
                elif set(outputSegments) == set(sixSegments):
                    finalOutput = finalOutput + '6'
                elif set(outputSegments) == set(nineSegments):
                    finalOutput = finalOutput + '9'

        sumOfoutputs = sumOfoutputs + int(finalOutput)

    print(sumOfoutputs)
    

def getNumbers(numbers, length):
    return [number for i, number in enumerate(numbers) if len(number) == length]

if __name__ == "__main__":
    main()
