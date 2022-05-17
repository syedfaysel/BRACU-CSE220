#reversing an array: in place (Algorithm)

from re import X


def reverse(source):

    i=0 #pointer at 0th index of source

    j=len(source)-1 #pointer at last index of source

    while(i<j):

        # print("i:",i,"j:",j)

        temp=source[i] #swapping the first and last elements
        # print("temp",temp, "source[i]",source[i])

        source[i]=source[j]

        # print("source[i]",source[i], "source[j]", source[j])

        source[j]=temp
        # print("source[j]:",source[j], "temp", temp)
        

        i=i+1

        j=j-1



a=[10,20,30,40,50]

reverse(a)

print(a)

#====================================================================
# Swapping variables (revision)

x, y = 10, 15

print(f"old x = {x}, old y = {y}")

temp = x
x = y # assigning the value of y to x

y = temp # assigning the value of temp to y (which was the value of x)

print(f"after swapping the values, new x = {x}, y = {y}")


