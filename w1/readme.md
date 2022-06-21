 # Week_1  
Lecture 1 : Linear Array, Array creation, iteration, copying, resize, reverse,shifting left-right, rotating left-right, insertion, deletion etc

Lecture 2: Circular Array, Forward and backward iteration, linearization, resizing, insertion and deletion.

## Introduction  

>**What are Data Structures?**  
In simple words, it is the way the data is stored in a computer.  

>**Types of Data Structures**  
 * Arrays
 * Linked Lists (LL)
 * Queues
 * Stacks  

 > **Prerequisites**  
 Sound knowledge on:  
 1 . Linear Arrays  
 2 . Object and Classes (OOP)

<br>

## Lecture_1: 

### Arrays  

>**Linear Array:**  
An Array is a collection of a fix number of items where all the items are of the same data type.  
Arrays consists of :  
**Element:** Each items stored in an array is called Element.  
**Index:** Each location of an element in an array has a numerical value, which is used to access its corresponding element. Index always starts from zero.  

<img src="https://tinyurl.com/2fba7bhn" alt= "linear Array" height="80%" width="350px"> 

<br>

> **Array Declaration & Initialization**  
In python we have built in list (similar to linear array but advance feature)  
Let's say `array = []` is a list / we say array for now. In general we have to mention the size of an array as we already know that array is fixed size.  
So, we write `array = [None]*size`, which creates an array of given size with None elements for now.  
Here `array` is the memory location/ reference.  
Using index, we can access the elements of an array.


```py

array = [None]*5  # created an array of size 5, with 5 None elements 
# size 5 means this array has 5 slots to store 5 data  
array[0] = 10
array[1] = 20
array[2] = 30
array[3] = 40
array[4] = 50

# Now, we stored 5 data in the 5 slots of the array,
# Here 0,1,2,3,4 are the indices. Notice that index starts at 0 
# and ends at size-1 (5-1=4)

print(array)

```
Output: [10,20,30,40,50]

### Traverse an Array  

> Accessing all elements or iterating through the array is called traversing.


To traverse an array we must use loop.
We need a loop variable which will work as index as well and starts from 0.

```py
array = [10,20,30,40,50]



```



## Lecture_2: