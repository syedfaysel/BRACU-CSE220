

def leftRotate(source,k):


    # store the k number of values first in a temp list
    temp = [0]*k
    for i in range(k):
        temp[i] = source[i]
    

    i = 0
    while(i<len(source)-k):
        source[i]= source[i+k]

        i+=1

    # rotating the values
    j = len(source)-k

    i =0
    while(j<len(source)):
        source[j]=temp[i]
        j+=1
        i+=1

    return(source)


arr1 = [1,2,3,4,5,6]

print(leftRotate(arr1,2))

