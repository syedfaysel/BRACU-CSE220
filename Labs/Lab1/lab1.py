# All the methods : 1 - 10

# Task 1

def shiftLeft(source,k):
    
    i = 0
    while(i<len(source)-k):
        source[i]= source[i+k]

        i+=1

 
    j = len(source) - k
    while(j<len(source)):
        source[j]=0
        j+=1  

    

arr1 = [10,20,30,40,50,60]

shiftLeft(arr1,3)

print(arr1)

#======================================
# Task 2

def rotateLeft(source,k):

    temp = [0]*k
    for i in range(k):
        temp[i] = source[i]

    i = 0

    # Using only single loop
    while(i<len(source)):
        if (i<len(source)-k):
            source[i]= source[i+k]
            i+=1
        else:
            source[i] = temp[i-(len(source) - k)]
            i +=1
        

arr1 = [10,20,30,40,50,60]

rotateLeft(arr1,3)
print(arr1)

#======================================

# Task 3

def shiftRight(source, k):
    i = len(source) - 1

    while(i>=k):

        source[i] = source[i-k]

        i-=1
    
    # setting the rest (k number of items) index values to zero
    for i in range(0,k):
        source[i] = 0

arr1 = [10,20,30,40,50,60]

shiftRight(arr1,3)
# Hence, array is reference data type, the actual value has been changed
print(arr1)

#==================================

# Task 4
# Rotate Right by k cells

def RotateRight(source, k):

    temp = [i for i in source[len(source)-k:]]

    #using for loop this time

    for i in range(len(source)-1,-1,-1):
        if (i>=k):
            source[i]= source[i-k]
        else:
            source[i] = temp[i]

    

arr1=[10,20,30,40,50,60]

print(RotateRight(arr1,3))



#===============================

# Task 5 
# remove item from array


def remove(source,size, index):
    for i in range(index, size-1):
        source[i] = source [i+1]
    
    source[size-1] = 0



arr1=[10,20,30,40,50,0,0]
remove(arr1,5,2)

print(arr1)


#======================================


# Task 6
# Remove all occurence 

def removeAll( source, size, element ):

    count = 0
    for i in range(size):
        if source[i] == element:
            count +=1

            for j in range(i,size):
                if (j<(size-1)-count):
                    source[j] = source[j+1]
                else:
                    source[j] = 0
                        

source=[10,2,30,2,50,2,2,0,0] 
removeAll(source,7,2)

print(source)


# Task 7
# Splitting an Array


def splitting_array(source):
    left_pan = [0]
    right_pan = []
    flag = None

    for i in range(len(source)):
        if i == 0:
            left_pan[i] = source[i]
            # splitting (i+1 -----> last index) to the right pan
            right_pan = source[i + 1 : (len(source))]
            # Checking if the sum of the values in both pan same or not
            if sum(left_pan) == sum(right_pan):
                flag = True
                break
            else:
                left_pan = []
        
                flag = False

        # if the index is not 0, 
        # splitting the values of the source array into both of the pan 
        # such way that (0----->i) in left pan & (i+1 ------> last index) in the right pan
        else:
            left_pan = source[0 : i + 1]
            right_pan = source[i + 1 : (len(source))]

            # Checking if the sum of the values in both pan same or not
            if sum(left_pan) == sum(right_pan):
                flag = True
                break
            else:
                flag = False
    return flag


arr1 = [2,1,1,2,1] 
splitting_array(arr1) #false

arr2 = [10,3,1,2,10] 
print(splitting_array(arr2)) # true

#=============================

# Task 8: Array series 

def array_series(n):

    array = [0]*(n*n)

    for i in range(1,n+1): 

        for j in range(1,i+1):
 
            array[(i*n)-j] = j

    return array


print(array_series(4))

#=============================

# Task 9
# Max bunch count

def max_bunch(source):

    count = 0
    max_count = 0

    for i in range(len(source)-1):

        if source[i] == source[i+1]:
            count +=1
            max_count = count
        else:
            count = 1

    return max_count


arr1 = [1,2,2]
print(max_bunch(arr1))

arr2 = [1,1,2,2,1,1,1,1]
print(max_bunch(arr2))


#================================

# Task 10: 
# Reptition 

def repetition(source): 

    flag = False

    items = [0]*len(source)
    count_repeat = [0]*len(source)

    repeated = 0 # number of repeated items

    for i in range(len(source)-1):
        bool = True
        count = 1

        
        for x in range(repeated):
            if (items[x]==source[i]):

                bool = False

        
        if bool == True:
            item = source[i]


            for y in range(i+1,len(source)):

                if source[y] == item:
                    count +=1
            
            if count>1:
                items[repeated] = item
                count_repeat[repeated] = count
                repeated+=1
    
    # Check at least 2 of the count of repetition are same or not
    for i in range(repeated-1):

            for j in range(i+1,repeated):

                if count_repeat[i] == count_repeat[j]:
                    flag = True
                    break

                    
    return flag
                    
arr1 = [1,2,3,2,3]

print(repetition(arr1))



#===========****=============#
