# print_array(), print_reverse() , custom method to print array

def print_array(source):
    i = 0
    while(i<len(source)):
        print(source[i])
        i+=1


def print_reverse(source):
    i = len(source) -1
    while(i>=0):
        print(source[i])
        i-=1


arr1 = [10,20,30,40,50]

arr2 = [1,2,3,4,5]

name = "Faysel"

print_array(arr1)
print_reverse(arr1)
print_array(name)
print_reverse(name)
