        newNode = Node(elem)
        current = self.head
        i = 0
        pred = None
        # if index is 0
        if (idx ==0):
            newNode.next = self.head # Assign
            self.head = newNode  # Update
        # if index is not 0]
        else:
            while(current):

                if (idx-1 == i):
                    pred = current
                    
                    newNode.next = pred.next
                    pred.next = newNode
                    break
                else:
                    i+=1
                current = current.next