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

mylist = [1, 8, 2, 7, 3, 6, 1, 6, 43, 56, 12, 74]
print(mylist)
mergesort(mylist)
print(mylist)
