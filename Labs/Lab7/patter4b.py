

def pattern(m, n):
    
    if (m == 0):
        return

    printSpace(m - 1)
    printSeq2(n - m + 1)
    print()

    pattern(m - 1, n)

def printSpace(m):
    
    if (m == 0):
        return

    print(" ", end=" ")
    printSpace(m - 1)

def printSeq2(m):

    if (m == 0):
        return

    printSeq2(m - 1)
    print(m, end =" ")

# pattern(5,5)




def fibo(n):

    if (n==1):
        return 0
    elif (n== 2):
        return 1
    else: 
        return fibo(n-1)+fibo(n-2)

# Test : method call
print(fibo(1))
print(fibo(2))
print(fibo(7))