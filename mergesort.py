#Description: Recursive and Iterative Merge Sort Implementations
#Author: Summer Gautier
#Date: May 11th 2020

import unittest

#Recursive
def recursiveSort(listOfItems: list) -> list:

    if(len(listOfItems) == 1):
        return listOfItems
    else:
        #Take into account odd/even length of lists
        lenHalf: int = (len(listOfItems)/2) if (len(listOfItems)%2 == 0) else (len(listOfItems)/2)-0.5

        #split list into halves
        list1: list = listOfItems[int(lenHalf):]
        list2: list = listOfItems[:int(lenHalf)]

        #make recursive call on rest of items
        list1 = recursiveSort(list1)
        list2 = recursiveSort(list2)
        return recursionMerge(list1, list2)
#Recursion Helper Method
def recursionMerge(listA: list, listB: list) -> list:
    listC: list = []
    #add the elements of listA and listB in order of whichever is greater
    while(len(listA) > 0 and len(listB) > 0):
        if(listA[0] > listB[0]):
            listC.append(listB[0])
            listB.pop(0)
        else:
            listC.append(listA[0])
            listA.pop(0)

    # if either listA or listB still have elements, add those to the end of listC
    while(len(listA) > 0):
        listC.append(listA[0])
        listA.pop(0)
    while(len(listB) > 0):            
        listC.append(listB[0])
        listB.pop(0)
    return listC


#Iterative
def iterativeSort(listOfItems: list, originalLength: int) -> list:
    currentLength = 1
    for currentLength in range (1, originalLength, currentLength):
        for leftIndex in range(0, originalLength, 2*currentLength):
            midIndex: int = min(leftIndex+currentLength-1, originalLength-1)
            rightIndex: int = min(leftIndex+2*currentLength-1, originalLength-1)
            iterationMerge(listOfItems, leftIndex, midIndex, rightIndex)
    return listOfItems
#Iterative Helper Method
def iterationMerge(subList: list, leftIndex: int, midIndex: int, rightIndex: int):
    leftListLength = midIndex - leftIndex + 1
    rightListLength = rightIndex - midIndex 
    leftList = [0] * leftListLength 
    rightList = [0] * rightListLength 
    for i in range(0, leftListLength): 
        leftList[i] = subList[leftIndex + i] 
    for i in range(0, rightListLength): 
        rightList[i] = subList[midIndex + i + 1] 

    i, j, k = 0, 0, leftIndex 
    while i < leftListLength and j < rightListLength: 
        if leftList[i] > rightList[j]: 
            subList[k] = rightList[j] 
            j += 1
        else: 
            subList[k] = leftList[i] 
            i += 1
        k += 1

    while i < leftListLength: 
        subList[k] = leftList[i] 
        i += 1
        k += 1

    while j < rightListLength: 
        subList[k] = rightList[j] 
        j += 1
        k += 1
  


#TEST SORT METHODS
class SortTest(unittest.TestCase):
    def test(self):
        sampleList: list = [25,5,14,28,9,16,7]
        self.assertEqual(iterativeSort(sampleList, len(sampleList)), [5,7,9,14,16,25,28])
        self.assertEqual(recursiveSort(sampleList), [5,7,9,14,16,25,28])

if __name__ == '__main__':
    print(str(unittest.main()))