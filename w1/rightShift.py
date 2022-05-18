#right shifting an array by one place

def rightShift(source):
    
    i = len(source) -1

    while(i>=1):
        source[i] = source[i-1]

        i-=1

    source[0] = 0
    print(source)

arr1 = [1,2,3,4]
# after doing rightShift it should look like: arr1 = [0,1,2,3]

rightShift(arr1)
print(arr1)