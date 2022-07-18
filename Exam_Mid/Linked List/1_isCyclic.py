

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

        current = self.head
        flag = False

        while(current):
            
            if (current.element == -1):
                flag = True
                break
            else:
                current.element = -1

            current = current.next
        return flag


# ================== Test Code ================
a = [10,30,40,50,60]

ll = Linkedlist(a)
ll.makeCyclic(4,2)

print(ll.isCyclic())

# print(ll.nodeAt(1).element)

            
# ============= zigzag merge list =================

l1 = Linkedlist([10,30,50])
l2 = Linkedlist([20,40,60])


def zigzagMerge(l1,l2):

    # print(l1.head.element)
    # print(l2.head.next.element)

    current1 = l1.head
    current2 = l2.head  
    # tail2 = l2.head
    
    while(current1 !=None):
        
        l2.head = l2.head.next
        current2.next = current1.next

        current1.next = current2

        current1 = current1.next.next
        current2 = l2.head
        # tail2 = tail2.next

        # return l1.head

        


# zigzagMerge(l1,l2)
# l1.printList()
