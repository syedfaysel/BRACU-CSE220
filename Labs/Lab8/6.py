

def binarySearch(arr, l, r, key):

    if (l >= r):
        return -1
    else:
        mid = (l + r)//2

        if(arr[mid] == key):
            return True
        
        elif (arr[mid]> key):
            binarySearch(arr, l, mid -1 , key)
        else:
            binarySearch(arr, mid+1, r, key)


a1 = [10, 20, 30, 40, 50]

print(binarySearch(a1,0, 4, 10))