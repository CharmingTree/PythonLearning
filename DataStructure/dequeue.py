class DeQueue:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None

    def __len__(self):
        cnt = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            cnt += 1
        return cnt

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def insertFront(self, data):
        newNode = DeQueue.Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
    
    def insertRear(self, data):
        newNode = DeQueue.Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
    
    def deleteFront(self):
        if self.head == None:
            return None
        else:
            p = self.head.data
            self.head = self.head.next
            return p
    
    def deleteRear(self):
        if self.head == None:
            return None
        elif self.__len__() == 1:
            p = self.head.data
            self.head = None
            return p
        else:
            temp = self.head
            for i in range(self.__len__()-2):
                temp = temp.next
            p = temp.next.data
            temp.next = None
            return p

            
    
    def peekFront(self):
        if self.head == None:
            return None
        else:
            return self.head.data
    
    def peekRear(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            return temp.data
    
    def __str__(self):
        p = []
        temp = self.head
        while temp != None:
            p.append(temp.data)
            temp = temp.next
        
        return p.__str__()

    

    

myDequeue = DeQueue()

print(myDequeue.isEmpty())

myDequeue.insertFront(10)
myDequeue.insertFront(20)
myDequeue.insertFront(30)
myDequeue.insertFront(40)
myDequeue.insertFront('aaa')
myDequeue.insertFront('bbb')
myDequeue.deleteRear()

print(myDequeue.isEmpty())
print(myDequeue.__str__())
print(myDequeue.peekFront())
print(myDequeue.peekFront())
print(myDequeue.peekRear())
print(myDequeue.peekRear())