
## Left shift 

"""
array = [1,2,3,4,5,6]
#left shifted by 1 place:
# after doing rightShift it should look like: 

leftShifted = [2,3,4,5,6,0]

"""

def leftShift(source,k):
    
    i = 0
    while(i<len(source)-k):
        source[i]= source[i+k]

        i+=k

 
    i =0
    while(j<len(source)):
        source[j]=0
        j+=1  

    return(source)


arr1 = [1,2,3,4,5,6]

print(leftShift(arr1,1))

