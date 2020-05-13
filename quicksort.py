#Description: Recursive and Iterative Quick Sort Implementations
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
        #sampleList1: list = [7,5,28,16,9,14,25]
        #self.assertEqual(iterativeSort(sampleList), [5,7,9,14,16,25,28])

        #test recursive method
        anotherList: list = [8,14,5,68,5,47,91]
        recursiveSort(anotherList, 0, len(anotherList)-1)
        self.assertEqual(anotherList, [5,5,8,14,47,68,91])

if __name__ == '__main__':
    print(str(unittest.main()))