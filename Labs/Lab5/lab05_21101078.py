# Student Name: Syed Faysel Ahammad Rajo
# Student ID: 21101078
# Section: 11
# Lab 05: Stack application - parentheses balancing
# Assignment : Final with resolved printing statement & efficient version

# Assignment : 
# array based Stack implementation

class arrStack:

    def __init__(self):

        self.list1 = [None]*20
        self.size = 0


    def push(self,element):
        
        if self.size == len(self.list1):
            print("Stack Overflow")
        else:        
            self.list1[self.size] = element
            self.size +=1


    def pop(self):
        if(self.size == 0):
            print("Stack underflow")
        else:
            temp = self.list1[self.size-1]
            self.list1[self.size-1] = None
            self.size -=1
            return temp


    def peek(self):
        if (self.size == 0):
            print("Stack Underflow")
        else:
            return self.list1[self.size-1]


# Linked list based Stack implementation

class Node:

    def __init__(self, e=None,n=None):
        self.element = e
        self.next = n

class llStack:

    # using a dummy headed linked list
    def __init__(self):
        self.head = Node()
        self.size = 0

    def push(self, element):

        newNode = Node(element)

        newNode.next = self.head.next
        self.head.next = newNode
        self.size +=1

    def pop(self):
        if (self.size==0):
            print("Stack underflow")
        else:
            # temp = (self.head.next.element)
            removed_node = self.head.next
            self.head.next = removed_node.next
            self.size -=1
            return removed_node.element


    def peek(self):
        if (self.size==0):
            print("Stack underflow")
        else:
            return (self.head.next.element)



# ============== Solving Problem: Parentheses Balance ============
# isBalanced() method : works for both array based stack (Task 1) & ll based stack (Task 2)

def isBalanced(exp, stackType):
    # exp = input()
    opn = "({["
    cls = ")}]"
    stack2 = stackType()
    flag = True

    idx = 0

    for item in exp:

        stackItem = [item,idx]

        if item in opn:
            stack2.push(stackItem)
            idx+=1
            
        elif item in cls:
            if stack2.size !=0:
                popped = stack2.pop()
                if opn.index(popped[0]) != cls.index(item):
                    message = (f"Error at character # {popped[1]+1}. '{popped[0]}'- not closed.")
                    flag = False
                    
                    break
                else:
                    idx +=1
                    continue
            else:
                message = (f"Error at character # {idx+1}. '{item}'- not opened.")
                flag = False
                break

        else:
            idx+=1
            continue

    print(exp)

    if (flag == True and stack2.size == 0):
        print("This expression is correct.")
    else:
        print("This expression is NOT correct.")
        print(message)

# =====================================================

exp = input()

#========== Task 1: array based solution ===============

isBalanced(exp,arrStack)

#========== Task 2 : linkedlist based solution ================

isBalanced(exp,llStack)

# Code executed successfully
