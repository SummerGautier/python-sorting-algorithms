#Description: Recursive and Iterative Merge Sort Implementations
#Author: Summer Gautier
#Date: May 11th 2020

import unittest



#TEST SORT METHODS
class SortTest(unittest.TestCase):
    def test(self):
        sampleList: list = [7,5,28,16,9,14,25]
        self.assertEqual(iterativeSort(sampleList), [5,7,9,14,16,25,28])
        self.assertEqual(recursiveSort(sampleList, len(sampleList)), [5,7,9,14,16,25,28])

if __name__ == '__main__':
    print(str(unittest.main()))