# Basic Linked List Manipulation Part 1

#------creating node class------

class Node:
    
    def __init__(self,e,n):
        self.element = e
        self.next = n

    
#----------Tester------------#

# Starting the node
head = None

#creating the nodes first

n1 = Node("10",None)
n2 = Node("20",None)
n3 = Node("30",None)

n1.next = n2
n2.next = n3

#assigning the head , reference to the list
head = n1







#---------count function -----------#

def countNode(h):
    count = 0
    n = h
    
    while(n!=None):
        count+=1
        n = n.next 

    return count



#----- Get Function ----------# 

def get(h,index):

    n = h
    count = 0
    
    while(n!=None):

        if(count == index):
             return n.element
             break
        count +=1
        n = n.next

    return -1   



#-----------Get Node at Function ---------#


def getNodeAt(h, size, index):

    if(index<0 or index>=size):

        return None

    n = h
    count = 0
    
    while(n!=None):
        
        if(count == index):
             return n
             break
        count +=1
        n = n.next


#-------------Set function------------#

def set(h, index, new_node_elm):
    
    n = h
    count = 0
    
    while(n!=None):
        
        if(count == index):
             n.element = new_node_elm
             break
        count +=1
        n = n.next


#--------------search function indexOf---------------

def indexOf(h, elem):
    n = h
    count = 0
    
    while(n!=None):

        if(n.element == elem):
             return count
             break

        count +=1
        n = n.next

    return -1 



#---------------xxxxx-----------------


totalNode = countNode(head)
nodeAddress = getNodeAt(head,3,1)
data = get(head, 1)


print(f"Total nodes in the list : {totalNode}")
print(f"Address of the node at given index: {nodeAddress}")
print(f"Element of the node at given index: {data}")

set(head,1,"100")

print(f"Updated Element of the node at given index: {get(head, 1)}")


search = indexOf(head,"100")
print(f"Index of the given element:{search}")
    