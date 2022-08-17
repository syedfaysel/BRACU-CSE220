# Lab 07 : Recursion
# Name : Syed Faysel Ahammad Rajo
# ID : 21101078
# Section : 11

#================ Task 01 =======================

#========== 01_a): Factorial (n!) using recursive algorithm =========

def fact(n):

    if (n==0 or n==1):
        return 1

    else: 
        return n*fact(n-1)

# Test : method call
print(fact(4))


#============ 01_b: n-th Fibonacci Number============

def fibo(n):

    if (n==1):
        return 0
    elif (n== 2):
        return 1
    else: 
        return fibo(n-1)+fibo(n-2)

# Test : method call
print(fibo(1))  # 1st term is 0, 
print(fibo(7)) # 7th term is 8

#============== 01_c: print elements of array =============

def printArray(array, l):
    if (l == len(array)):
        return
    else:
        print(array[l], end=" ")
        return printArray(array, l+1)

printArray([10,20,30,40],0)

print()

#============ 01_d: power(base, n) using recursion =========

def powerN(base, n):
    if (n==1):
        return base
    else:
        return base*powerN(base,n-1)

print(powerN(3,2))

# ============= 01_d: base to the power n alternative & efficient solution:===========
#  
def expoN(base, n):
    if (n == 0):
        return 1
    else:
        if (n % 2 == 0):
            return (expoN(base, n/2) * expoN(base, n/2))
        else:
            return (base * expoN(base, n//2) * expoN(base, n//2))

# Test Method: expoN
print(expoN(3, 2)) # expected output: 27


# =========================== Task 02 =======================

#Node Class 

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# for test purpose
i4 = Node(40)
i3 = Node(30,i4)
i2 = Node(20,i3)
i1 = Node(10,i2)


# =========02_a: Decimal to Binary  (divide by 2, returns the mods)========

def decToBin(n):
    if (n == 0):
        print(0,end='')
        return 
    else:
        decToBin(n//2)
        print(n % 2 , end='')

# test method decToBin(n) : 
decToBin(3)
print()

#============ 02_b : Sum of elements of Linked List===============

def sum(node):

    if (node.next == None):
        return node.data
    else: 
        return node.data + sum(node.next)

print(sum(i1))

# ========== 02_c: print ll elements in reverse order ==========

def printRev(node):

    if (node.next == None):
        print(node.data, end=" ")
    else:
        printRev(node.next)
        print(node.data, end=" ")

# Test: method call 
printRev(i1)

#-----------
print()
# ======================== Task 03 =============================
# Hocbuilder
def hocBuilder(height):
    if (height<1):
        return 0
    elif (height==1):
        return 8
    else:
        return 5 + hocBuilder(height - 1)

print(hocBuilder(2))

# ========================= Task 04 ==============================

# ========= 04_a : pattern printing using recursion ========== 

def printPattern(m):
    if (m == 0):
        print(" ")
    else:
        printPattern(m-1)
        printSeq(m)

def printSeq(m):
    if (m == 0):
        print(" ")
    else:
        printSeq(m-1)
        print(m,end=" ")

printPattern(5)

#------------
print() # empty sapce/ newline

# ======== 4_b: Pattern printing ==================

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

pattern(5,5)
print() # empty space

# ====================== Task 05 =========================

# Task 5: Investment
class FinalQ: 

    def print(self,array,idx): 
        if(idx<len(array)): 
            profit = self.calcProfit(array[idx]) 
            #TO DO 
            print(f"{idx+1}. Investent: {array[idx]}; Profit: {profit}")
            self.print(array, idx+1)

    def calcProfit(self,investment): 
        if (investment <= 25000):
            return 0.0
        elif (investment > 25000 and investment <= 100000):
            return 45 + self.calcProfit(investment-1000)
        elif (investment > 100000):
            return 80 + self.calcProfit(investment-1000)
        else:
            return 0

# --------- Tester ---------
array = [25000,100000,250000,350000] 
f = FinalQ() 
f.print(array,0)


# ============ END =================



