#Description: Recursive and Iterative Insertion Sort Implementations
#Author: Summer Gautier
#Date: May 8th 2020

import unittest

#RECURSIVE
def recursiveSort(listOfItems: list, startIndex: int, endIndex: int) -> list:
    if(startIndex == endIndex):
        return [listOfItems[startIndex]]
    else:
        subList: list = recursiveSort(listOfItems, startIndex-1, endIndex)
        largest: bool = True
        for index, item in enumerate(subList):
            if(item > listOfItems[startIndex]):
                subList.insert(index, listOfItems[startIndex])
                largest = False
                break
        if(largest):
            subList.append(listOfItems[startIndex])
        
        return subList

#ITERATIVE
def iterativeSort(listOfItems: list) -> list:
    for index, item in enumerate(listOfItems):
        for subListIndex in range(0, index):
            if(listOfItems[subListIndex] > item):
                del listOfItems[index]
                listOfItems.insert(subListIndex, item)
                break

    return listOfItems

#TEST SORT METHODS
class SortTest(unittest.TestCase):
    def test(self):
        sampleList = [18,5,6,1,7,3,23,8,10]
        self.assertEqual(iterativeSort(sampleList), [1,3,5,6,7,8,10,18,23]),
        self.assertEqual(recursiveSort(sampleList, len(sampleList)-1, 0), [1,3,5,6,7,8,10,18,23])

if __name__ == '__main__':
    print(str(unittest.main()))