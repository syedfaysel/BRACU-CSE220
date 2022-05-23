#forward printing a circular array

# better approach

def printForward(c,start,size):

    index=start

    i=0

    while(i<size):

        print(c[index],end=" ")

        index=(index+1)%len(c)

        i=i+1



circularArray=[40,50,0,0,0,0,0,0,10,20,30] #creating a circular array with start 8 and size 5

printForward(circularArray,8,5)


#============================================
# self Practice

def forwardPrint(cArr, start, size):
    
    index = start
    
    for i in range(0,size):

        print(cArr[index],end=" ")

        # index +=1
        # if index==len(cArr):
        #     index = 0   

        #line 37-39, condition can be shortened as 
        index=(index+1)%len(cArr)

#====================================

forwardPrint(circularArray,8,5)