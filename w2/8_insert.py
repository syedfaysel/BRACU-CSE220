

def insert(cirArray, start,size, elem, pos):

    # number of shifted elements
    nShifts = size - pos
    # Inserted Index
    index = (size + pos)%len(cirArray)

    # right shift 
    fr = (start + size -1)%len(cirArray)

    to = (fr+1)%len(cirArray)

    # backward iteration
    for i in range(nShifts):

        cirArray[to] = cirArray[fr]

        to = fr
        fr = fr -1

        if (fr<0):
            fr = len(cirArray) - 1

    print(cirArray)

    cirArray[index] = elem
    print(cirArray)

arr = [40,50,60,None,None,10,20,30]


insert(arr,5,6, 100,2)

    