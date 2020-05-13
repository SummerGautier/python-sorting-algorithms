# python-sorting-algorithms
Recursive and Iterative implementation of various sorting algorithms
## Algorithms
+ Selection sort
    - Look in the list for the smallest item and swap that item with the item at the first index of the list. Repeat this for the second smallest, third smallest, etc. until the list is sorted.
+ Insertion sort
    - With the first two items of the list, sort them in the correct order. Then, insert the third item into the sorted subset of the list. Repeat with the fourth item, fifth item, etc. Keep inserting items into the sorted subset until all items in the list have been sorted.
+ Bubble sort
    - For each item (A) at a position 'n' in the list, compare it with the item (B) in position 'n+1' in the list. If the item A is greater than item B, then swap items A and B. Following this system, after one pass, the largest unsorted item will make it's final position in the unsorted array. Repeat until the entire list is sorted.
+ Merge sort
    - Divide the the list into halves until you've reached the smallest possible list (a single item). Then, sort the sublists and merge them until you've created a complete sorted list
+ Quick sort
    - Choose a pivot item in the array from which you can partition the array into sections. The pivot item will end up in it's final position in the array after one pass of the pivot sort. This follows as all items larger will be to the right and all items smaller than the pivto will be to the left. There are a couple of ways to pick a pivot:
        1. Pick first element of the array as pivot
        2. Pick last element of the array as pivot
        3. Pick a random element as pivot
        4. Pick a median as pivot (the middle most number among the first, last, and middle element)
