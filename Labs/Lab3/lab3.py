class Node:

    def __init__(self, e= None, n = None):
        self.element = e
        self.next = n

    
class LinkedList:

    def __init__(self, a):

        head = Node(a[0])
        self.head = head
        tail = self.head
        
        for i in range(1, len(a)):

            newNode = Node(a[i])
            tail.next = newNode
            tail = newNode 
            
#============================
    def printList(self):
        #To do
        current = self.head
        
        while(current):

            print(current.element, end = ",")
            current = current.next
        print("\n")

#============================
    def countNode(self):
        # To Do
        count = 0

        current = self.head
        while(current):

            count +=1
            current = current.next
        
        return count

#============================
    def nodeAt(self, idx):
        
        if (idx<0 or idx>self.countNode()):
            return None

        count = 0
        current = self.head
        while(current):

            if (count == idx):
                return (current)
            else:
                count +=1

            current = current.next

#============================
    def getNode(self,idx):
        i = 0
        pred = None
        current = self.head
        while(current):

            if (idx == i):
                pred = current
                return pred
            else:
                i+=1
            current = current.next

#============================

    # Using getNode() method
    def insert(self,elem,idx):

        if (idx<0 or idx>self.countNode()):
            return None

        # index = idx
        pred = self.getNode(idx-1)
        newNode = Node(elem)
        
        if idx == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            #  pred = self.getNode(idx-1)   
                newNode.next = pred.next
                pred.next = newNode 

    # without using getNode()
    def insert2(self, elem, idx):

        newNode = Node(elem)
        current = self.head
        i = 0
        pred = None
        # if index is 0
        if (idx ==0):
            newNode.next = self.head # Assign
            self.head = newNode  # Update
        # if index is not 0]
        else:
            while(current):

                if (idx-1 == i):
                    pred = current
                    
                    newNode.next = pred.next
                    pred.next = newNode
                    break
                else:
                    i+=1
                current = current.next

        
 
#======================Test Code ============================

print("////// Test 01 //////")
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1) # Creates a linked list using the values from the array
# head will refer to the Node that contains the element from a[0]

h1.printList() # This should print: 10,20,30,40
print(h1.countNode()) # This should print: 4

print("////// Test 02 //////")
# returns the reference of the Node at the given index. For invalid idx return None.
myNode = h1.nodeAt(1)
print(myNode.element) # This should print: 20. In case of invalid index This will generate an Error.


print("////// Test 09 //////")
a6 = [10,20,30,40]
h6 = LinkedList(a6) # uses theconstructor where a is an built in list
h6.printList() # This should print: 10,20,30,40.  
    
# inserts Node containing the given element at the given index. Check validity of index.
h6.insert(85,0)
h6.printList() # This should print: 85,10,20,30,40.  
h6.insert(95,3)
h6.printList() # This should print: 85,10,20,95,30,40.  
h6.insert(75,6)
h6.printList() # This should print: 85,10,20,95,30,40,75.
# ==============
print("////////self Test 09////////")
h6.insert2(13,5)
h6.printList()
        
