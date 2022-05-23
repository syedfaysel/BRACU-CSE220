# Week 2
## L3: Circular Array




### Array Traversal
> Forward printing a circular array 


> Thumb Rule 1:   
one variable as loop controler  
(How many times the loop will run)  
Different variable for index of circualr array

<br>

> Thumb Rule 2:  
Whenever you increment the index of a circualr array, always mod the incremented value with the circular array's length.  
`index=(index+1)%len(circularArray)`


```py
#forward printing a circular array


def printForward(c,start,size):

    index=start

    i=0

    while(i<size):

        print(c[index],end =" ")

        index=(index+1)%len(c)

        i=i+1



circularArray=[40,50,0,0,0,0,0,0,10,20,30] #creating a circular array with start 8 and size 5

printForward(circularArray,8,5)
```

> output:  `10 20 30 40 50  `
