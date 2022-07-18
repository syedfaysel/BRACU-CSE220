# array based implementation

class Stack:

    def __init__(self):

        self.list1 = [None]*20
        self.size = 0


    def push(self,element):
        
        if self.size == len(self.list1):
            print("Stack OVerflow")
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

#============Tester================
# dummyStack = Stack()

# dummyStack.push(10)
# print(dummyStack.peek())
# dummyStack.pop()
# print(dummyStack.peek())

# ============== Solving Problem: Parentheses Balance ============

# given an expression in string

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

# ============================================

exp1 = "1+2*(3/4)"
exp2 = "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
exp3 = "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
exp4 = "1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"

isBalanced(exp1)
isBalanced(exp2)
isBalanced(exp3)
isBalanced(exp4)