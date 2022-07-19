

class Node:

    def __init__(self,e=None,n=None):
        self.element = e
        self.next = n

class Linkedlist:
    
    def __init__(self, a):

        if (type(a) == Node):
            self.head = a

        # Array based ll
        else:
            self.head = Node(a[0])
            tail = self.head

            for i in range(1,len(a)):

                newNode = Node(a[i])
                tail.next = newNode
                tail = newNode

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
        

    # Count the number of nodes in the list
    def countNode(self):
        # To Do
        count = 0
        current = self.head
        while(current):

            count +=1
            current = current.next
        
        return count

    # Node at method
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

    # makyCyclic method: 
    def makeCyclic(self, startIdx, endIdx):

        self.nodeAt(startIdx).next = self.nodeAt(endIdx)



    def isCyclic(self):

        if (self.head==None):
            return False

        current = self.head
        flag = False

        while(current):
            
            if (current.element == -1):
                # flag = True
                # break
                return True
            else:
                current.element = -1

            current = current.next
        # return flag
        return False



    def reverse(self, m, n):
        dummy = Node()
        dummy.next = self.head

        # 1: traverse till m node
        leftPred = dummy
        current = self.head
        for i in range(m):
            leftPred = current
            current = current.next

        # 2: traverse from m node to n node & reverse
        # at this point current refers to m node & leftPred refers to node before the m node
        # reverse from left to right
        pred = None
        for i in range(n-m+1):
            temp = current.next
            current.next = pred
            pred = current
            current = temp

        # 3: Update the pointers /iterators
        leftPred.next.next = current
        leftPred.next = pred
        
        return dummy.next


    # Reverse Between another veresion: 
    # Most efficient code for reverse between 
    def reverse2(self, start, end):

        if (self.head ==None or start==end):
            return self.head
        dummy = Node()
        dummy.next = self.head

        nodeBeforeSublist = dummy 
        # pos = 0,same as while(pos<start)
        for i in range(start):
            nodeBeforeSublist = nodeBeforeSublist.next

        workingPtr = nodeBeforeSublist.next
        # same as while(start<end):
        for i in range(start,end):
            nodeToBeExtracted = workingPtr.next
            workingPtr.next = nodeToBeExtracted.next

            nodeToBeExtracted.next = nodeBeforeSublist.next
            nodeBeforeSublist.next = nodeToBeExtracted
        return dummy.next

    # Reverse Between another veresion (Easy to understand of efficient version): 
    # Most efficient code for reverse between 
    def reverse3(self, start, end):

        if (self.head ==None or start==end):
            return self.head
        dummy = Node()
        dummy.next = self.head
        current = dummy.next # current is same as workingPtr
        pred = dummy #nodeBeforeSublist is same as pred


        # pos = 0,same as while(pos<start)
        for i in range(start):
            pred = pred.next
            current = current.next

        # same as while(start<end):
        for i in range(start,end):
            temp = current.next
            current.next = temp.next

            temp.next = pred.next
            pred.next = temp
        return dummy.next



# ================== Test Code ================
a = [10,30,40,50,60]

ll = Linkedlist(a)
# ll.makeCyclic(4,2)

print(ll.isCyclic())

ll2 = Linkedlist([10,20,30,40,50])
ll2.printList()
ll2.reverse3(1,3)
ll2.printList()
            
# ============= zigzag merge list =================

l1 = Linkedlist([10,30,50])
l2 = Linkedlist([20,40,60])


def zigzagMerge(l1,l2):

    current1 = l1.head
    current2 = l2.head  
    tail2 = l2.head
    
    while(current1 !=None):
        
        # l2.head = l2.head.next   # use tail(as a reference of l2.head)
        tail2 = tail2.next # 1: update the iterator(head) of the 2nd list
        current2.next = current1.next  # 2: assign current.next as current2.next
        current1.next = current2 # 3. update current1.next with the value from 2nd list

        current1 = current1.next.next # 4: update the iterator of the 1st list
        # current2 = l2.head
        current2 = tail2  # update the iterator (Node to be merged) of 2nd list


    return l1.head

merged = Linkedlist(zigzagMerge(l1,l2))
l1.printList()
merged.printList()
# both are same
