import unittest
def mergesort(mylist):
    mergesort2(mylist, 0, len(mylist)-1)
    
def mergesort2(mylist, first, last):
    if first < last:
        middle = (first + last)//2
        mergesort2(mylist, first, middle)
        mergesort2(mylist, middle+1, last)
        merge(mylist, first, middle, last)
        
def merge(mylist, first, middle, last):
    Left = mylist[first:middle+1]
    Right = mylist[middle+1:last+1]
    Left.append(99999999)
    Right.append(99999999)
    i = j = 0
    for k in range (first, last+1):
        if Left[i] <= Right[j]:
            mylist[k] = Left[i]
            i += 1
        else:
            mylist[k] = Right[j]
            j += 1

def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

class mergetest(unittest.TestCase):

    def testOne(self):
        mergesort(mylist)
        self.assertEqual(mylist, sort(array))
    def testTwo(self):
        mergesort(mylist1)
        self.assertEqual(mylist1, sort(array1))
    def testThree(self):
        mergesort(mylist2)
        self.assertEqual(mylist2, sort(array2))
    def testFour(self):
        mergesort(mylist3)
        self.assertEqual(mylist3, sort(array3))
    def testFive(self):
        mergesort(mylist4)
        self.assertEqual(mylist4, sort(array4))


array = [1, 8, 2, 7, 3, 6, 1, 6, 43, 56, 12, 74]
mylist = [1, 8, 2, 7, 3, 6, 1, 6, 43, 56, 12, 74]
mylist1 = []
mylist2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
mylist3 = [345, 678967, 123, 6574, 1232, 565, 909, 23, 89, 32]
mylist4 = ['dsf', 'tfdh', 'awer', 'rst']
array1 = []
array2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
array3 = [345, 678967, 123, 6574, 1232, 565, 909, 23, 89, 32]
array4 = ['dsf', 'tfdh', 'awer', 'rst']
print(mylist)
#mergesort(mylist)
print(mylist)
unittest.main()
