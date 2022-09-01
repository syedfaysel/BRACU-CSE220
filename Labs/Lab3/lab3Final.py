# Name: Syed Faysel Ahammad Rajo
# Student ID: 21101078
# Lab 3: Linked List

class Node:
    def __init__(self, e=None, n=None):
        self.element = e
        self.next = n



class LinkedList:

    def __init__(self, a):
    #  Design the constructor based on data type of a. If 'a' is built in python list then
    #  Creates a linked list using the values from the given array. head will refer
    #  to the Node that contains the element from a[0]
    #  Else Sets the value of head. head will refer
    # to the given LinkedList

    # Hint: Use the type() function to determine the data type of a

        # To Do
        if (type(a)== Node):
            self.head = a
        
        else:
            self.head = Node(a[0])
            tail = self.head
            
            for i in range(1, len(a)):

                newNode = Node(a[i])
                tail.next = newNode
                tail = newNode 

    # ====================================
    # Count the number of nodes in the list
    def countNode(self):
        # To Do
        count = 0

        current = self.head
        while(current):

            count +=1
            current = current.next
        
        return count
    # ==================================== 
    # Print elements in the list
    def printList(self):
        # To Do
        current = self.head
            
        while(current):
            # Printing style
            if (current.next==None):
                print(current.element)
            else:
                print(current.element, end = ",")
            # Update the iterator (Node in this case)    
            current = current.next
        
    #=====================================

    # returns the reference of the Node at the given index. For invalid index return None.
    def nodeAt(self, idx):
        # To Do
        if (idx<0 or idx>=(self.countNode())):
            return None

        count = 0
        current = self.head
        while(current):

            if (count == idx):
                return (current)
            else:
                count +=1

            current = current.next

    #=====================================
    
    # returns the element of the Node at the given index. For invalid idx return None.
    def get(self, idx):
        # To Do
        # index validation
        if (idx<0 or idx>=(self.countNode())):
            return None
        # setting up a counter as index
        count = 0
        current = self.head
        while(current):
            
            if (count == idx):
                return current.element
            else:
                count+=1
            
            current = current.next
    #=====================================
    # updates the element of the Node at the given index. 
    # Returns the old element that was replaced. For invalid index return None.
    # parameter: index, element
    def set(self, idx, elem):
        # To Do
        if (idx<0 or idx>=self.countNode()):
            return None
        
        current = self.head
        index = 0
        while(current):
            if (index == idx):
                old = current.element
                current.element = elem
                return old
            else:
                index+=1
            current = current.next

    #===========================================
    # returns the index of the Node containing the given element.
    # if the element does not exist in the List, return -1.
    def indexOf(self, elem):
        # To Do
        index = 0
        current = self.head
        while(current):
            if (current.element == elem):
                return index
            else:
                index+=1
            #updating the iterator
            current = current.next
        return -1
    
    # returns true if the element exists in the List, return false otherwise.
    def contains(self, elem):
        # To Do
        flag = False
        current = self.head
        while(current):
            if (current.element == elem):
                flag = True
                return flag
            else:
                flag = False
            current = current.next
        return flag

    # Makes a duplicate copy of the given List. Returns the reference of the duplicate list.
    def copyList(self):
        # To Do
        current = self.head
        copyH = Node(current.element)
        copyT = copyH
        
        current = current.next

        while(current):

            new = Node(current.element)
            copyT.next = new
            copyT = new

            current = current.next
        return copyH


    # Makes a reversed copy of the given List. Returns the head reference of the reversed list.
    def reverseList(self):
        # To Do
        
        current = self.head
        revH = Node(current.element)
        current = current.next

        while(current):
            new = Node(current.element)

            new.next = revH #assign 
            revH = new #update 
            
            current = current.next
            
        return revH


    #=========================================
    # inserts Node containing the given element at the given index
    # Check validity of index.
    def insert(self, elem, idx):
        # To Do
        # index validation: in case of insert :(ide<0 or idx>(self.countNode())); cause we can insert even after the last index
        if (idx<0 or idx>(self.countNode())):
            return None

        # if index is valid:-->   
        newNode = Node(elem)
        current = self.head
        i = 0
        # predecessor (Node before the idx position)
        pred = None
        # if index is 0 (Inserting at beginning)
        if (idx ==0):
            newNode.next = self.head # Assign
            self.head = newNode  # Update
        # if index is not 0
        else:
            while(current):

                if (idx-1 == i):
                    pred = current
                    
                    newNode.next = pred.next # Assign
                    pred.next = newNode # update
                    break
                else:
                    i+=1
                current = current.next

    #=======================================

    # removes Node at the given index. returns element of the removed node.
    # Check validity of index. return None if index is invalid.
    def remove(self, idx):
        # To Do
        if (idx<0 or idx>=self.countNode()):
            return None
        
        current = self.head
        i = 0
        pred = None
        # if index is 0
        if (idx ==0):
            removed = self.head.element
            self.head = self.head.next

            return removed

        # if index is not 0
        else:
            while(current):

                if (idx-1 == i):
                    pred = current
                    removed = pred.next.element
                    # newNode.next = pred.next
                    pred.next = current.next.next
                    
                    return removed
                else:
                    i+=1
                current = current.next
    
    #========================================
    # Rotates the list to the left by 1 position.
    def rotateLeft(self):
        # To Do
        prevH = self.head
        self.head = prevH.next

        tail = prevH
        while(tail.next):
            tail = tail.next
        tail.next = prevH
        prevH.next = None
    
    #========================================
    # Rotates the list to the right by 1 position.
    def rotateRight(self):
        # To Do
        pred = None # predecessor
        prevH = self.head # interate prevH

        # Iteratig till the 2nd last node
        # since we have to find predecessor
        while(prevH.next):
            pred = prevH #
            prevH = prevH.next
            
            # pred = predecessor node
            # prevH = the middle node (Our desired head)
            # prevH.next = last node

        prevH.next = self.head  
        self.head = prevH

        # assigning self.head as the prevH.next (as 2nd node)
        # updating original head to our desired head (prevH)

        pred.next = None
        # pred.next = None makes the pred tail node
        



#//////////////////Test Code//////////////////////

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


print("////// Test 03 //////")
# returns the element of the Node at the given index. For invalid idx return None.
val = h1.get(2)
print(val) # This should print: 30. In case of invalid index This will print None.
    

print("////// Test 04 //////")
    
# updates the element of the Node at the given index. 
# Returns the old element that was replaced. For invalid index return None.
# parameter: index, element
         
print(h1.set(1,85)) # This should print: 20
h1.printList() # This should print: 10,85,30,40.
print(h1.set(15,85)) # This should print: None
h1.printList() # This should print: 10,85,30,40.


print("////// Test 05 //////")
# returns the index of the Node containing the given element.
# if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that doesn't exists in the list this will print -1.
    

print("////// Test 06 //////")
# returns true if the element exists in the List, return false otherwise.
ask = h1.contains(40)
print(ask) # This should print: True.


print("////// Test 07 //////")
a2 = [10,20,30,40,50,60,70]
h2 = LinkedList(a2) # uses the constructor where a is an built in list
h2.printList() # This should print: 10,20,30,40,50,60,70.  
# Makes a duplicate copy of the given List. Returns the head reference of the duplicate list.
copyH=h2.copyList() # Head node reference of the duplicate list
h3 = LinkedList(copyH) # uses the constructor where a is head of a linkedlist 
h3.printList() # This should print: 10,20,30,40,50,60,70.  
    
    
print("////// Test 08 //////")
a4 = [10,20,30,40,50]
h4 = LinkedList(a4) # uses theconstructor where a is an built in list
h4.printList() # This should print: 10,20,30,40,50.  
# Makes a reversed copy of the given List. Returns the head reference of the reversed list.
revH=h4.reverseList() # Head node reference of the reversed list
h5 = LinkedList(revH) # uses the constructor where a is head of a linkedlist 
h5.printList() # This should print: 50,40,30,20,10.  


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


print("////// Test 10 //////")
a7 = [10,20,30,40,50,60,70]
h7 = LinkedList(a7) # uses theconstructor where a is an built in list
h7.printList() # This should print: 10,20,30,40,50,60,70.  
    
# removes Node at the given index. returns element of the removed node.
# Check validity of index. return None if index is invalid.
    
print("Removed element:",h7.remove(0)) # This should print: Removed element: 10
h7.printList() # This should print: 20,30,40,50,60,70.  
print("Removed element: ",h7.remove(3)) # This should print: Removed element: 50
h7.printList() # This should print: 20,30,40,60,70.  
print("Removed element: ",h7.remove(4)) # This should print: Removed element: 70
h7.printList() # This should print: 20,30,40,60. 


print("////// Test 11 //////")
a8 = [10,20,30,40]
h8 = LinkedList(a8) # uses theconstructor where a is an built in list
h8.printList() # This should print: 10,20,30,40.  
    
# Rotates the list to the left by 1 position.
h8.rotateLeft()
h8.printList() # This should print: 20,30,40,10.  
    
    
print("////// Test 12 //////")
a9 = [10,20,30,40]
h9 = LinkedList(a9) # uses theconstructor where a is an built in list
h9.printList() # This should print: 10,20,30,40.  
    
# Rotates the list to the right by 1 position.
h9.rotateRight()
h9.printList() # This should print: 40,10,20,30.