class Queue:
    def __init__(self,n):
        self.ms=n
        self.cs=0
        self.arr=[0]*n
        self.front=0
        self.rear=n-1

    def isEmpty(self):
        return self.cs == 0

    def isFull(self):
        return self.cs==self.ms

    def enqueue(self,data):
        if not self.isFull():
            self.rear = (self.rear+1)%self.ms
            self.arr[self.rear]=data
            self.cs+=1

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%self.ms
            self.cs-=1

    def getFront(self):
        return self.arr[self.front]

A=Queue(6)
A.enqueue(1)
A.enqueue(2)
A.enqueue(3)
A.enqueue(4)
A.enqueue(5)
A.enqueue(6)
A.dequeue()
A.dequeue()
A.dequeue()
print(A.getFront())
print(A.arr)
