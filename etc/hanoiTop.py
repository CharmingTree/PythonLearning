
class stack:
    def __init__(self, name):
        self.head = None
        self.name = name
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __str__(self):
        
        resultString = []
        temp = self.head
        while temp != None:
            resultString.append(temp.data)
            temp = temp.next
        return resultString.__str__()
    def push(self, data):
        newNode = stack.Node(data)
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
        elif self.head.next == None:
            result = self.head.data
            self.head == None
            return result
        else:
            prev = None
            temp = self.head
            while temp.next != None:
                prev = temp
                temp = temp.next
            result = temp.data
            prev.next = None
            return result


def display(A : stack, B : stack, C : stack):
    
    tLst = []
    tLst.append(A)
    tLst.append(B)
    tLst.append(C)
    tempA = None
    tempB = None
    tempC = None

    for i in tLst:
        if i.name == 'A':
            tempA = i.head
        if i.name == 'B':
            tempB = i.head
        if i.name == 'C':
            tempC = i.head

    lstA = []
    #tempA = A.head
    while tempA != None:
        lstA.append(tempA.data)
        tempA = tempA.next
    
    lstA.reverse()

    lstB = []
    #tempB = B.head
    while tempB != None:
        lstB.append(tempB.data)
        tempB = tempB.next
    
    lstB.reverse()

    lstC = []
    #tempC = C.head
    while tempC != None:
        lstC.append(tempC.data)
        tempC = tempC.next

    lstC.reverse()

    length = max(len(lstA), len(lstB), len(lstC))
    print("=====================================")
    for i in range(length):
        _a = lstA[i] if len(lstA) > i else 0
        _b = lstB[i] if len(lstB) > i else 0
        _c = lstC[i] if len(lstC) > i else 0
        print(f"{_a}\t{_b}\t{_c}")
    print("=====================================\n")
    
def hanoi(n : int, f : stack, t : stack, tmp : stack):

    
    if n == 1:
        t.push(f.pop())
        display(f, t, tmp)
        return
    else:
        hanoi(n-1, f, t, tmp)
        t.push(f.pop())
        display(f, t, tmp)
        hanoi(n-1, tmp, f, t)


a = stack('A')
b = stack('B')
c = stack('C')

# a.push(3)
# a.push(2)
# a.push(1)

print(a.__str__())
#hanoi(3, a, b, c)