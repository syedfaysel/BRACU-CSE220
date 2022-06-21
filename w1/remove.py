

def removeElem(source, size, index):

    # doing left shift after the given index
    for i in range(index, size):
        source[i] = source [i+1]

    return source

# ==================
arr1 = [10,20,30,40,50,0,0,0]

print(removeElem(arr1,5,2))