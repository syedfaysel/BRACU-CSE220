# Assignment : 

# Linked list based implementation

class Node:

    def __init__(self, e=None,n=None):
        self.element = e
        self.next = n

class Stack:

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

#============Tester================


# ============== Solving Problem: Parentheses Balance ============


def isBalanced(exp):

    opn = "({["
    cls = ")}]"
    stack2 = Stack()
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
exp5 = "{}"

isBalanced(exp5)

isBalanced(exp1)
isBalanced(exp2)
isBalanced(exp3)
isBalanced(exp4)

