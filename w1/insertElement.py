# Inserting an element on a given index, 
# Inserting doesn't mean replacing
# To insert we have to right shift all other elements by 1 place after the given index


def insert(source,index, value, size):

    # check if the index is valid/is there any empty slot to insert
    print(source)
    # if size == len(source), there is no space
    if (size==len(source)):
        print("No slot available in array")
        return
    # invalid index
    if (index<0 or index>size):
        print("Invalid Index")
        return

    # if the above condtion is true: first do right shift, then insert

    #right shift starts from ending /last index
    lastIdx = size-1


    # for i in range(lastIdx,index-1,-1):
        
    #     source[i+1]= source[i]

    # while loop explains it better
    # the condition is: right shifting till given position

    while(lastIdx>=index):
        source[lastIdx+1]= source[lastIdx]
        lastIdx -=1

    # insert the value on given index after shifting all other items   
    source[index]= value

    print(source)


array = [10,20,30,40,0,0]

insert(array,1,15,4)

