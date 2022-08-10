
class ArrayQueue:

    def __init__(self,arr,st,sz):

        self.size = sz
        self.start = st
        self.capacity = len(arr)
        self.array = arr



    def enqueue(self, item):
        lastIdx = (self.start+self.size-1)%self.capacity
        nextAvailablePos = (self.start+self.size)%self.capacity

        self.array[nextAvailablePos] = item
        self.size +=1

    def dequeue(self):
        
        removed = self.array[self.start]
        self.array[self.start] = None
        self.start +=1
        return removed

    def peek(self):
        return self.array[self.start]


# ======================


ar1 = [None, None, None, None, None, None]

q1 = ArrayQueue(ar1,0,0)

q1.enqueue(29)
q1.enqueue(10)
q1.enqueue(34)
q1.enqueue(45)
q1.enqueue(34)
print(q1.array)

print(q1.peek())
print(q1.dequeue())
print(q1.peek())
print(q1.array)