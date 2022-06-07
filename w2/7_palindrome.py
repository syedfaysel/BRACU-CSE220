

def isPalindrome(source, size, start):

    palindrome = False

    index = start
    # j = last index = (start +size -1)%len(source)
    j = (start +size -1)%len(source)

    for i in range(size//2):

        if (source[index]== source[j]):
            palindrome = True
        else: 
            palindrome = False
            break
        
        index = (index+1)%len(source)

        j = j-1

        if (j<0):
            j = len(source)-1

    return palindrome

 # =========

arr1 = [1,2,3,2,1,0,0,0]

arr2 = [1,1,3,2,1,0,0,0]
print(isPalindrome(arr1,5,0))
print(isPalindrome(arr2,5,0))