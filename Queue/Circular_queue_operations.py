from collections import deque
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=deque([-1]*k)
        self.length=k
        self.head=0
        self.tail=0 
        

    def enQueue(self, value: int) -> bool:
        if self.head==self.tail and -1 not in self.queue:
            return False
        
        else:
            self.queue[self.tail]=value
            self.tail=((self.tail)+1)%self.length
            return True
        
    def deQueue(self) -> bool:
        if self.queue[self.head]==-1:
            return False
        else:
            self.queue[self.head]=-1
            self.head=((self.head)+1)%self.length
            return True

    def Front(self) -> int:
        return self.queue[self.head]
        

    def Rear(self) -> int:
        return self.queue[((self.tail)-1)%self.length]

    def isEmpty(self) -> bool:
        if self.queue[self.head]==-1:
            return True

    def isFull(self) -> bool:
        if self.head==self.tail and -1 not in self.queue:
            return True
