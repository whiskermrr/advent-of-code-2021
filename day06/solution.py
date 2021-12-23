import os
from collections import deque

def main():
    lanternfishList = list(map(int, open('input.txt', 'r').readline().strip().split(',')))
    solution(80, lanternfishList, 6, 8)
    solution(256, lanternfishList, 6, 8)

def solution(noOfDays, lanternfishList, cycleLength, newCycleLength):
    totalNoOfFishes = len(lanternfishList)
    fishList = []
    
    for i in range(newCycleLength + 1):
        fishList.append(0)

    fishList = deque(fishList)

    for lanternfish in lanternfishList:
        fishList[lanternfish] = fishList[lanternfish] + 1


    for i in range(0, noOfDays):
        noOfNewFishes = fishList[0]
        fishList.rotate(-1)
        fishList[cycleLength] = fishList[cycleLength] + noOfNewFishes
        fishList[newCycleLength] = noOfNewFishes
        totalNoOfFishes = totalNoOfFishes + noOfNewFishes
        

    print(totalNoOfFishes)

if __name__ == "__main__":
    main()
