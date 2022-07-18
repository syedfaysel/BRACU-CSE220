# Student Name: Syed Faysel Ahammad Rajo
# Student ID: 21101078
# Section: 11
# Lab 05: Stack application - parentheses balancing
# Assignment : Final with resolved printing statement & efficient version
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



# ============== Solving Problem: Parentheses Balance ============
# isBalanced() method : works for both array based stack & ll based stack 

def isBalanced(exp, stackType):

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

# ============================================

exp1 = "1+2*(3/4)"
exp2 = "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
exp3 = "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
exp4 = "1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"

#========== Task 1 ===============

isBalanced(exp1,arrStack)
isBalanced(exp2,arrStack)
isBalanced(exp3,arrStack)
isBalanced(exp4,arrStack)

#========== Task 2 ================

# isBalanced(exp1,llStack)
# isBalanced(exp2,llStack)
# isBalanced(exp3,llStack)
# isBalanced(exp4,llStack)

# Code executed successfully
