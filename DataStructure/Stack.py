
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        print('---')
        return str(self.data)

class StackWithLinkedList:

    def __init__(self):
        self.head = None
        self.top = 0
    
    def __str__(self):
        
        if self.top <= 0:
            return ''
        temp = self.head
        s = []
        while temp != None:
            s.append(temp.data)
            temp = temp.next
        return s.__str__()
    
    def __len__(self)->int:
        return self.top

    def push(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            
            temp.next = newNode
        self.top += 1
    
    def pop(self):
        print('>>>>', self.top)
        if self.head == None or self.top == 0:
            raise IndexError("Stack is Empty!")
        
        if self.top == 1:
            p = self.head.data
            self.head = None
            self.top -= 1
            return p
        else:
            temp = self.head
            prev = None
            p = None
            for i in range(self.top-1):
                prev = temp
                temp = temp.next
            p = temp.data
            prev.next = None
            self.top -= 1

        return p
            
    def peek(self):

        if self.head == None:
            raise IndexError("Stack is Empty!")
        
        temp = self.head
        p = None
        for i in range(self.top-1):
            temp = temp.next
        p = temp.data

        return p


myStackWithLL = StackWithLinkedList()

print(myStackWithLL.__len__())

myStackWithLL.push(10)
myStackWithLL.push(20)



print(myStackWithLL.peek())

myStackWithLL.pop()
myStackWithLL.pop()
#print(myStackWithLL)

class Stack:

    def __init__(self, size):
        self.head = None
        self.size = size
        self.arr = [None for i in range(size)]
        self.position = 0

    def __str__(self):
        return str(self.arr)
    
    ## peek, push, pop, sizeof, isEmpty, isFull? 

    def __len__(self) ->int:
        return len(self.arr)

    def peek(self):
        return self.arr[self.position]

    def push(self, data):
        if not self.size > self.position:
            raise IndexError()
        
        self.arr[self.position] = data
        self.position += 1

    def isEmpty(self)->bool:
        if self.position == 0:
            return True
        else:
            return False
    
    def pop(self):
        if not self.position >= 0:
            raise IndexError("stack is empty")
        
        p = self.arr[self.position-1]
        self.arr.pop(self.position-1)
        self.position -= 1

        return p


myStack = Stack(10)

# print(myStack.isEmpty())

# myStack.push('aaaa')
# myStack.push('bbbb')
# myStack.push('cccc')
# myStack.push('dddd')
# myStack.push('eeee')
# myStack.push('ffff')
# myStack.push('gggg')
# myStack.push('hhhh')
# myStack.push('iiii')
# myStack.push('jjjj')

# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()

# print(myStack)