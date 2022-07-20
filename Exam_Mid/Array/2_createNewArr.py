

def sumArray(arr1,arr2):

    newArray = [None]*len(arr1)
    for i in range(len(arr1)):
        if (arr1[i]==None):
            arr1[i] = 0

        if (arr2[len(arr1)-i-1]==None):
            arr2[len(arr1)-i-1] = 0

        newArray[i] = arr1[i]+ arr2[len(arr1)-i-1]
    return newArray

# ================================Test Cases: 

a1 = [10,20,30,40]
a2 = [30,10,None,40]

print(sumArray(a1,a2))
