

#  Linear array  


def sortLinear(source, size):


    for i in range(size): 

        for j in range(i+1, size):

            if source[i]>source[j]:

                #  do swap
                temp = source[i]
                source[i] = source[j]
                source[j] = temp
            
    return source 



# Sorting Circular array

def sortCircular(source, size, start):

    # index = start

    #index i= (i+start)%len(source)
    # j = (j+start)%len(source)

    for i in range(size): 

        for j in range(i+1, size):

            if source[i]>source[j]:

                #  do swap
                temp = source[i]
                source[i] = source[j]
                source[j] = temp
            
            # Update
            i = (i+start)%len(source)
            j = (j+start)%len(source)
            
    return source 



# =========================

arr1 = [4,5,2,3,0,0]
arr2 = [5,8,0,6,10]

print(sortLinear(arr1,4))


print(sortCircular(arr2,4,3))
