from enum import Enum

class SimStatusType(Enum):
    arrival = 1
    start = 2
    end = 3

class SimCustomerType:
    def __init__(self, arrivalTime, serviceTime):
        self.status : SimStatusType = SimStatusType.arrival
        self.arrivalTime = arrivalTime
        self.serviceTime = serviceTime
        self.startTime = 0
        self.endTime = 0
    def __str__(self)->str:
        result = f"status : {self.status}, arrivalTime : {self.arrivalTime}, serviceTime : {self.serviceTime}, startTime : {self.startTime}, endTime : {self.endTime}"
        return result
    
    def printSimCustomer(self, currentTime):
        print(f'[{currentTime}]', end=' ')
        if self.status == SimStatusType.arrival:
            print('고객 도착')
        elif self.status == SimStatusType.start:
            print('서비스 시작', end='')
            print(f', 도착-{self.arrivalTime}, 대기 시간-{self.startTime - self.arrivalTime}')
        else:
            print('서비스 종료', end='')
            print(f', 도착-{self.arrivalTime},시작-{self.startTime} 대기 시간-{self.startTime - self.arrivalTime}, 서비스 시간-{self.endTime - self.startTime}')

class queue:
    
    def __init__(self):
        self.head = None
    def __str__(self):
        if self.head == None:
            return ''
        else:
            st = []
            temp = self.head
            while( temp != None):
                st.append(temp.data.__str__())
                temp = temp.next
        return st.__str__()
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    # insertFront, insertTail, deleteFront, deleteTail, peekFront, peekTail

    def __len__(self):
        if self.head == None:
            return 0
        else:
            cnt = 0
            temp = self.head
            while temp != None:
                temp = temp.next
                cnt += 1
            return cnt

    def isEmprt(self)->bool:
        if self.head == None:
            return True
        else:
            return False
    
    def insertFront(self, data):
        newNode = queue.Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def insertTail(self, data):
        newNode = queue.Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
    
    def deleteFornt(self):
        if self.head == None:
            return None
        else:
            resultData = self.head.data
            self.head = self.head.next
        return resultData
    
    def deleteTail(self):
        if self.head == None:
            return None
        elif self.__len__() == 1:
            resultData = self.head.data
            self.head = None
            return resultData
        else:
            temp = self.head
            prev = None
            while temp.next != None:
                prev = temp
                temp = temp.next
            resultData = temp.data
            prev.next = None
            return resultData

    def peekFront(self):
        if self.head == None:
            return None
        else:
            return self.head.data
    
    def peekTail(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            return temp.data

def processArrival(currentTime, arrivalQueue : queue, waitQueue: queue):
    
    while not arrivalQueue.isEmprt():

        arrivalNode : SimCustomerType = arrivalQueue.peekFront()

        if arrivalNode.arrivalTime == currentTime:
            waitQueue.insertTail(arrivalNode)
            arrivalNode.printSimCustomer(currentTime)

            arrivalQueue.deleteFornt()
        else:
            break

def processServiceNodeStart(currentTime, waitQueue : queue):
    result : SimCustomerType = None
    serviceNode : SimCustomerType = None

    if not waitQueue.isEmprt():
        serviceNode = waitQueue.deleteFornt()

        if serviceNode != None:
            serviceNode.status = SimStatusType.start
            serviceNode.startTime = currentTime
            serviceNode.printSimCustomer(currentTime)

            result = serviceNode

    return result


def processServiceNodeEnd(currentTime, serviceNode : SimCustomerType, serviceUserCount, totalWaitTime):
    endTime = 0
    waitTime = 0
    result : SimCustomerType = None
    
    if serviceNode == None or serviceUserCount == None or totalWaitTime == None:
        return None
    
    endTime = serviceNode.startTime + serviceNode.serviceTime

    if endTime <= currentTime:
        waitTime = serviceNode.startTime - serviceNode.arrivalTime

        serviceUserCount[0] += 1
        totalWaitTime[0] += waitTime

        serviceNode.status = SimStatusType.end
        serviceNode.endTime = currentTime
        serviceNode.printSimCustomer(currentTime)

        result = None
    else:
        result = serviceNode
    
    return result

def printWaitQueueStatus(currentTime, waitQueue : queue):
    print(f'[{currentTime}], 현재 대기 고객 수 : [{waitQueue.__len__()}]')

def printReport(waitQueue : queue, serviceUserCount, totalWaitTime):
    print('REPORT')
    print(f'서비스 고객 수 : {serviceUserCount[0]} ')
    if serviceUserCount[0] > 0:
        print(f'평균 대기 시간 : {totalWaitTime[0] / serviceUserCount[0]}')
    print(f'현재 대기 열의 고객 수 : {waitQueue.__len__()}')
currentTime = 0
endTime = 10
serviceUserCount = [0]
totalWaitTime = [0]

arrivalQueue = queue()
waitQueue = queue()
serviceQueue = queue()
serviceNode : SimCustomerType = None

a = SimCustomerType(0, 3)
b = SimCustomerType(2, 2)
c = SimCustomerType(4, 1)
d = SimCustomerType(6, 1)
e = SimCustomerType(8, 3)
arrivalQueue.insertTail(a)
arrivalQueue.insertTail(b)
arrivalQueue.insertTail(c)
arrivalQueue.insertTail(d)
arrivalQueue.insertTail(e)

for i in range(endTime):
    currentTime = i
    processArrival(currentTime, arrivalQueue, waitQueue)

    # 서비스 종료 처리
    if serviceNode != None:
        serviceNode = processServiceNodeEnd(currentTime, serviceNode, serviceUserCount, totalWaitTime)
    
    if serviceNode == None:
        serviceNode = processServiceNodeStart(currentTime, waitQueue)
    
    printWaitQueueStatus(currentTime, waitQueue)

printReport(waitQueue, serviceUserCount, totalWaitTime)