#Description: Recursive and Iterative Bubble Sort Implementations
#Author: Summer Gautier
#Date: May 8th 2020

import unittest

#Recursive
def recursiveSort(listOfItems:list, size: int)-> list:
    if(size == 1):
        return listOfItems
    for index,item in enumerate(listOfItems):
            #if this is the last array index, skip this iteration
            if(index == (len(listOfItems)-1)):
                continue
            #if the item is greater than the next, it needs to swap
            if(item > listOfItems[index + 1]):
                swapRequired = True
                listOfItems = swap(listOfItems, index, index + 1)
    return recursiveSort(listOfItems, size-1)

#Iterative
def iterativeSort(listOfItems: list) -> list:
    while(True):
        swapRequired: bool = False
        for index,item in enumerate(listOfItems):
            #if this is the last array index, skip this iteration
            if(index == (len(listOfItems)-1)):
                continue
            #if the item is greater than the next, it needs to swap
            if(item > listOfItems[index + 1]):
                swapRequired = True
                listOfItems = swap(listOfItems, index, index + 1)
        if(swapRequired == False):
            break
    return listOfItems

#helper method
def swap(listOfItems: list, firstIndex: int, secondIndex: int) -> list:
    temp: int = listOfItems[firstIndex]
    listOfItems[firstIndex] = listOfItems[secondIndex]
    listOfItems[secondIndex] = temp
    return listOfItems

#TEST SORT METHODS
class SortTest(unittest.TestCase):
    def test(self):
        sampleList: list = [7,5,28,16,9,14,25]
        self.assertEqual(iterativeSort(sampleList), [5,7,9,14,16,25,28])
        self.assertEqual(recursiveSort(sampleList, len(sampleList)), [5,7,9,14,16,25,28])

if __name__ == '__main__':
    print(str(unittest.main()))