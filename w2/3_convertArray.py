#converting a linear array to a circular array

def circularize(linear,start,size):

    circular=[0]*len(linear)

    index=start

    i=0

    while(i<size):

        circular[index]=linear[i]

        index=(index+1)%len(circular) 

        i=i+1

    return circular



linear=[10,20,30,40,50,0,0,0,0,0,0]

circ=circularize(linear,8,5)

print(circ)