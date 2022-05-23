# Week 2
## L3: Circular Array




### Array Traversal

**Forward printing a circular array**


> **Thumb Rule 1**:   
one variable as loop controler  
(How many times the loop will run)  
Different variable for index of circualr array

<br>

> **Thumb Rule 2**:  
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

<br>

**Reverse printing a cricular array:**  

> **Thumb Rule 3:**  
`last index = (start + size - 1)% array's length `

```py
#reverse printing a circular array

def printReverse(c,start,size):

    index=(start+size-1)%len(c)

    i=0

    while(i<size):

        print(c[index])

        index=index-1

        #No shortcut
        if(index<0):

            index=len(c)-1  

        i=i+1


circularArray=[40,50,0,0,0,0,0,0,10,20,30] 
#creating a circular array with start 8 and size 5

printReverse(circularArray,8,5)

```


> **Thumb Rule 4:**   
Whenever you decrement the index of a circular array, always keep a check whether it becomes negative. If it does, point it to the end of the array.  

```py
if(index<0):
    index=len(c)-1 
```
