#Description: Recursive and Iterative Merge Sort Implementations
#Author: Summer Gautier
#Date: May 11th 2020

import unittest

#Recursive
def recursiveSort(listOfItems: list) -> list:
    if(len(listOfItems) == 1):
        return listOfItems

    #Take into account odd/even length of lists
    lenUpperHalf: int = (len(listOfItems)/2) if (len(listOfItems)%2 == 0) else (len(listOfItems)/2)+0.5;
    lenLowerHalf: int = (len(listOfItems)/2) if (len(listOfItems)%2 == 0) else (len(listOfItems)/2)-0.5;

    #split list into halves
    list1: list = listOfItems[:int(lenUpperHalf)]
    list2: list = listOfItems[int(lenLowerHalf):]

    #make recursive call on rest of items
    list1 = recursiveSort(list1)
    list2 = recursiveSort(list2)
    return merge(list1, list2)

#Iterative


#Helper Method
def merge(listA: list, listB: list) -> list:
    listC: list = []
    #add the elements of listA and listB in order of whichever is greater
    for a, b in zip(listA, listB):
        if(listA[0] > listB[0]):
            listC.append(listB[0])
            listB.pop(0)
        else:
            listC.append(listA[0])
            listA.pop(0)
    return listA

    # if either listA or listB still have elements, add those to the end of listC
    for a in listA:
        listC.append(listA[0])
        listA.pop(0)
    for b in listB:            
        listC.append(listB[0])
        listB.pop(0)
    return listC

#TEST SORT METHODS
class SortTest(unittest.TestCase):
    def test(self):
        sampleList: list = [7,5,28,16,9,14,25]
        #self.assertEqual(iterativeSort(sampleList), [5,7,9,14,16,25,28])
        self.assertEqual(recursiveSort(sampleList), [5,7,9,14,16,25,28])

if __name__ == '__main__':
    print(str(unittest.main()))