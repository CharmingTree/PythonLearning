class Queue:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
    
    # peek, push, pop, isEmpty, getlength, str

    def __str__(self):
        if self.head == None:
            return ''
        else:
            p = []
            temp = self.head
            while temp != None:
                p.append(temp.data)
                temp = temp.next
            return p.__str__()
            

    def push(self, data):

        newNode = Queue.Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
    
    def pop(self):

        if self.head == None:
            return None
        else:
            p = self.head.data
            self.head = self.head.next
            return p
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def __len__(self):
        cnt = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            cnt += 1
        
        return cnt


myQ = Queue()

print(myQ)

myQ.push('aa')
myQ.push(10)
print(len(myQ))
print(myQ.isEmpty())
print(myQ.pop())
print(myQ.pop())
print(len(myQ))
print(myQ.isEmpty())