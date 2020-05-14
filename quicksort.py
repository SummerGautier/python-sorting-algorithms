#Description: Recursive Quick Sort Implementation
#Author: Summer Gautier
#Date: May 12th 2020

import unittest

#Recursive
def recursiveSort(listOfItems: list, lowIndex: int, highIndex: int) -> list:
    if(lowIndex < highIndex):
        pivotIndex: int = partition(listOfItems, lowIndex, highIndex)
        recursiveSort(listOfItems, lowIndex, pivotIndex -1)
        recursiveSort(listOfItems, pivotIndex+1, highIndex)


#Partition METHOD
def partition(listOfItems: list, startIndex: int, endIndex: int) -> int:
    pivot = listOfItems[endIndex]
    pivotIndex = (startIndex - 1)
    for index in range(startIndex, endIndex):
        if(listOfItems[index] < pivot):
            pivotIndex +=1 
            listOfItems = swap(listOfItems, pivotIndex, index)
    listOfItems = swap(listOfItems, pivotIndex+1, endIndex)
    return (pivotIndex+1)
    
#Iterative


#HELPER METHODS
def swap(listOfItems: list, firstIndex: int, secondIndex: int) -> list:
    temp: int = listOfItems[firstIndex]
    listOfItems[firstIndex] = listOfItems[secondIndex]
    listOfItems[secondIndex] = temp
    return listOfItems

#TEST SORT METHODS
class SortTest(unittest.TestCase):
    def test(self):

        #test recursive method
        sampleList: list = [8,14,5,68,5,47,91]
        recursiveSort(sampleList, 0, len(sampleList)-1)
        self.assertEqual(sampleList, [5,5,8,14,47,68,91])

if __name__ == '__main__':
    print(str(unittest.main()))