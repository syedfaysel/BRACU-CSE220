#right rotating an array by one place

def rightRotate(source):
    temp = source[len(source)-1]  # same as source[-1] in python
    i = len(source) -1

    while(i>=1):
        source[i] = source[i-1]

        i-=1

    source[0] = temp  # assigning the last value of source at 0th index.
    print(source)

arr1 = [1,2,3,4]
# after doing rightRotate it should look like: arr1 = [4,1,2,3]

rightRotate(arr1)

