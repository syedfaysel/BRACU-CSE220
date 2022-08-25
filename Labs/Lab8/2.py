

def insertionSort(a, l, r):
    if  l>=r:
        return
    else:
        insertionSort(a, l, r-1)
        temp = a[r+1]
        j = r + 1
        while(j >= 0 and temp > a[j]):
            a[j+1] = a[j]
            j -=1
        a[j+1] = temp


a = [10, 30, 20, 40]
insertionSort(a, 3,  )
print(a)

# use doubley linked list since we need to traverse in both way
# def listSort(list, head, tail):
#     if (tail.prev == None):
#         return
    
#     else:
#         listSort(list, )
