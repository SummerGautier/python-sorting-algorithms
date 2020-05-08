#Description: Recursive and Iterative Selection Sort Implementations
#Author: Summer Gautier
#Date: May 8th 2020

import unittest

#RECURSIVE
def recursiveSort(listOfItems: list, OuterIndex: int, endIndex: int) -> list:
    indexOfMinimum = OuterIndex;
    if(OuterIndex == endIndex):
        for innerIndex in range(OuterIndex, endIndex):
            if(listOfItems[innerIndex] < listOfItems[indexOfMinimum]):
                indexOfMinimum = innerIndex
        listOfItems = swap(listOfItems,OuterIndex, indexOfMinimum)
        return listOfItems
    else:
        listOfItems = recursiveSort(listOfItems, OuterIndex+1, endIndex)
        for innerIndex in range(OuterIndex, endIndex):
            if(listOfItems[innerIndex] < listOfItems[indexOfMinimum]):
                indexOfMinimum = innerIndex
        listOfItems = swap(listOfItems,OuterIndex, indexOfMinimum)
        return listOfItems

#ITERATIVE
def iterativeSort(listOfItems: list) -> list:
    for OuterIndex in range(0, len(listOfItems)):
        indexOfMinimum = OuterIndex
        for innerIndex in range(OuterIndex, len(listOfItems)):
            if(listOfItems[innerIndex] < listOfItems[indexOfMinimum]):
                indexOfMinimum = innerIndex
        listOfItems = swap(listOfItems,OuterIndex, indexOfMinimum)
    return listOfItems

def swap(listOfItems: list, firstIndex: int, secondIndex: int) -> list:
    temp = listOfItems[firstIndex]
    listOfItems[firstIndex] = listOfItems[secondIndex]
    listOfItems[secondIndex] = temp
    return listOfItems

#TEST SORT METHODS
class SortTest(unittest.TestCase):
    def test(self):
        sampleList = [5,18,6,1,7,3,23,8]
        self.assertEqual(iterativeSort(sampleList), [1,3,5,6,7,8,18,23])
        self.assertEqual(recursiveSort(sampleList, 0, len(sampleList)-1), [1,3,5,6,7,8,18,23])

if __name__ == '__main__':
    print(str(unittest.main()));