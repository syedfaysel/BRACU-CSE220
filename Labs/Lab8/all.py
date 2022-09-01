

def bubbleSort(a,n):

    if (n == 0):
        return
    
    else:
        for i in range(n-1):
            if (a[i] > a[i+1]):

                # swap
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp

        bubbleSort(a, n-1)

a = [1,3,2,5,4]
# bubbleSort(a, len(a))
# print(a)



# Node  class
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# ll class

class Linkedlist:
    def __init__(self,a):
        self.head = a[0]
        current = self.head

        for i in range(1,len(a)):
            newNode = Node(a[i], None)
            current.next = newNode
            current = newNode

    def printList(self):
        current = self.head
        while(current !=None):
            if (current.next == None):
                print(current.data)
            else:
                print(current.data, end=" ")


# test ll

l1 = Linkedlist(a)
# l1.printList


# n4 = Node(5)
# n3 = Node(10, n4)
# n2 = Node(10, n3)
# n1 = Node(10, n2)

def bubbleSort(node):

    if (node.next == None):
        return
    
    else:
        current = node
        while(current.next != None):
            if (current.data > current.next.data):


                # swap
                temp = current
                current = current.next
                current.next = temp

        bubbleSort(node.next)


