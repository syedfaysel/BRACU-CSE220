# find_min

def findMin(arr, l, r):
    if (l == r):
        return l
    else:
        mid = (l + r)//2
    
        minLeft = findMin(arr, l, mid - 1)
        minRight = findMin(arr, mid + 1, r)

        minIdx = minLeft

        if (arr[minRight] < arr[minLeft]):
            minIdx = minRight
        return minIdx

a = [20, 10, 40, 30]

print(findMin(a, 0, len(a)-1))