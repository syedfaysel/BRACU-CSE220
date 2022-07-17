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
            print("Stack Underflow")
        else:
            # temp = (self.head.next.element)
            removed_node = self.head.next
            self.head.next = removed_node.next
        
            return removed_node.element


    def peek(self):
        if (self.size==0):
            print("Stack Underflow")
        else:
            return (self.head.next.element)


#==============Test Code================

# stack1 = Stack()
# stack1.push(10)
# stack1.push(20)
# stack1.push(30)
# stack1.push(40)
# print(stack1.peek())
# print(stack1.pop())
# print(stack1.peek())


# ============= Solving assignment question ================

def isBalanced(exp):

    opn = "({["
    cls = ")}]"
    stack1 = Stack()
    flag = True

    for item in exp:
        if item in opn or item in cls:
            if item in opn:
                stack1.push(item)
            else:
                if stack1.size !=0:
                    popped = stack1.pop()
                    if opn.index(popped) != cls.index(item):
                        flag = False
                        break
                    else:
                        continue
                else:
                    flag = False
                    break

        else:
            continue

    print(exp)

    if flag == True:
        print("This expression is correct.")
    else:
        print("This expression is NOT correct.")


exp1 = "1+2*(3/4)"
exp2 = "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
exp3 = "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
exp4 = "1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"

isBalanced(exp1)
isBalanced(exp2)
isBalanced(exp3)
isBalanced(exp4)