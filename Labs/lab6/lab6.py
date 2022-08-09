# Lab 06 : key index search , sorting & hash table

# Name: Syed Faysel Ahammad Rajo 
# Student ID: 21101078
# Section : 11

## ------------------- Task 01 -----------------------

class KeyIndex: 

    def __init__(self,a):

        # Auxiliary Array: to work with negative values
        auxA = [None]*len(a)
        for i in range(len(a)):
            auxA[i] = a[i]-min(a) # substracting min value to start with 0

        self.a = a
        self.k = [None]*(max(auxA)+1)

        for i in auxA:
            if (self.k[i]==None):
                self.k[i]=1
            else:
                self.k[i]+=1


    def search(self, val):
        flag = False
        for i in self.a:
            if i==val:
                flag = True
                break
        return flag


    def sort(self):
        x = 0
        for i in range(len(self.k)):
            if (self.k[i]!=None):
                for j in range(self.k[i]):
                    # Adjust the min value that was substracted
                    self.a[x] = i + min(self.a)
                    x+=1
        return (self.a)
            
# ----------------Tester statement--------------

ar1 = [4,-2,3,4,7,4]
k1 = KeyIndex(ar1)
print(k1.sort())
print(k1.search(-2))


## ---------------------- Task 02 (Hash Table) --------------------

def makeHashTable(arr):

    # the hashTable can have max 9 item since index % 9 is upto 0 - 8
    hashTable = [None]*9 

    for i in arr:
        dgts = 0
        cnst = 0
        for x in i:
            if (x>='A' and x<='Z' and x!='A' and x!='E' and x!='I' and x!='O' and x!='U'):
                cnst+=1
            elif (x>="0" and x<="9"):
                dgts += int(x)

        # given hash function: (consonant*24 + summation of the digits)%9
        idx = (cnst*24 + dgts) % 9
        # print(idx)

        # Storing strings to the hashTable as the index found from hash function
        # Linear probbing (using circular array) to deal collision
        if (hashTable[idx] == None):
            hashTable[idx] = i
        else:
            while (hashTable[idx]!= None):
                idx = (idx + 1)%len(arr)
            hashTable[idx] = i 

    return hashTable

# ================ Tester Code ===============

arr = ["ST1E89B8A32","ST1F89B8A33","ST1E89B8A36","ST1E89A8A32"]
print(makeHashTable(arr))
