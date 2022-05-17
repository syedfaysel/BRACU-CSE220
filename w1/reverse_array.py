#reversing an array: out of place

def reverse(source):

    dest=[0]*len(source)  #creating an empty array named dest having the same length as source

    i=0 #pointer at 0th index of source

    j=len(dest)-1 #pointer at last index of dest

    while(i<len(source)):

        dest[j]=source[i] #copying element from source to dest

        i=i+1

        j=j-1

    return dest #returning the array containing the elements in reverse order



a=[10,20,30,40,50]

b=reverse(a)

print(b)