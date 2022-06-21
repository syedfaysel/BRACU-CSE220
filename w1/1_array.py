from re import A


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

#=====================

# Better approach is using loop

