#Description: Recursive and Iterative Selection Sort Implementations
#Author: Summer Gautier
#Date: May 8th 2020

import unittest

#RECURSIVE
def recursiveSort(listOfItems: list, primaryIndex: int, endIndex: int) -> list:
    minimumIndex = primaryIndex;
    if(primaryIndex == endIndex):
        for secondaryIndex in range(primaryIndex, endIndex):
            if(listOfItems[secondaryIndex] < listOfItems[minimumIndex]):
                minimumIndex = secondaryIndex
        listOfItems = swap(listOfItems,primaryIndex, minimumIndex)
        return listOfItems
    else:
        listOfItems = recursiveSort(listOfItems, primaryIndex+1, endIndex)
        for secondaryIndex in range(primaryIndex, endIndex):
            if(listOfItems[secondaryIndex] < listOfItems[minimumIndex]):
                minimumIndex = secondaryIndex
        listOfItems = swap(listOfItems,primaryIndex, minimumIndex)
        return listOfItems

#ITERATIVE
def iterativeSort(listOfItems: list) -> list:
    for primaryIndex in range(0, len(listOfItems)):
        minimumIndex = primaryIndex
        for secondaryIndex in range(primaryIndex, len(listOfItems)):
            if(listOfItems[secondaryIndex] < listOfItems[minimumIndex]):
                minimumIndex = secondaryIndex
        listOfItems = swap(listOfItems,primaryIndex, minimumIndex)
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