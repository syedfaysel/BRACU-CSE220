#right shifting and right rotating an array by k places



def rightShift(source, k):

    i = len(source) - 1

    while(i>=k):

        source[i] = source[i-k]

        i-=1
    
    # setting the rest (k number of items) index values to zero
    for i in range(0,k):
        source[i] = 0

#===========================================================

def rightRotate(source,k):

    # fist, creating a temporary array to hold last k number of elements
    j = len(source) - (k)
    temp = []

    # for i in range(j, len(source)):
    #     temp.append(source[i])

    # using while loop as alternative:

    while(j<len(source)):
        temp.append(source[j])
        j+=1


    # rotating the values
    i = len(source) - 1
    while(i>=k):

        source[i] = source[i-k]

        i-=1
    
    # rotating last k number of elements to the first
    for i in range(0,k):
        source[i] = temp[i]

# ==========================================================


    
arr1 = [10,20, 30,40, 50]
rightShift(arr1, 2)
print(f"arr1 = {arr1} after doing right shift")
#  resulting array should look like : [0,0,10,20,30]

arr2 = [1,2,3,4,5,6]

rightRotate(arr2, 3)
# resulting array should look like: [4,5,6,1,2,3]
print(f"arr2 = {arr2} after doing right rotate")


