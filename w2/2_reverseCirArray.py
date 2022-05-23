#reverse printing a circular array


def printReverse(c,start,size):

    index=(start+size-1)%len(c)

    i=0

    while(i<size):

        print(c[index])

        index=index-1

        if(index<0):

            index=len(c)-1  

        i=i+1



circularArray=[40,50,0,0,0,0,0,0,10,20,30] 
#creating a circular array with start 8 and size 5

printReverse(circularArray,8,5)
