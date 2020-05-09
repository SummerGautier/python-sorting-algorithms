#Description: Recursive and Iterative Insertion Sort Implementations
#Author: Summer Gautier
#Date: May 8th 2020

import unittest

#RECURSIVE
#IN PROGRESS .....

#ITERATIVE
def iterativeSort(listOfItems: list) -> list:
    sortedList = []

    for outerIndex in range(0, len(listOfItems)):
        indexOfMinimum = 0
        for innerIndex in range(0, len(listOfItems)):
            if(listOfItems[innerIndex] < listOfItems[indexOfMinimum]):
                indexOfMinimum = innerIndex
        sortedList.append(listOfItems[indexOfMinimum])
        del(listOfItems[indexOfMinimum])

    print(sortedList)
    return sortedList

#TEST SORT METHODS
class SortTest(unittest.TestCase):
    def test(self):
        sampleList = [5,18,6,1,7,3,23,8,10]
        self.assertEqual(iterativeSort(sampleList), [1,3,5,6,7,8,10,18,23]),
        #self.assertEqual(recursiveSort(sampleList, 0, len(sampleList)-1), [1,3,5,6,7,8,18,23])

if __name__ == '__main__':
    print(str(unittest.main()))