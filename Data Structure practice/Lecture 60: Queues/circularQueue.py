# coding ninjas - circular queue

class CircularQueue:
    def __init__(self, n):
        # Initialize your data structure.
        self.front = -1
        self.rear = -1
        self.n = n
        self.queue = [None]*n

    # Enqueues 'X' into the queue. Returns true if it gets pushed into the queue, and false otherwise.
    def enqueue(self, value):
        # Write your code here.
        #print(self.rear, self.front)
        if ((self.rear + 1)%self.n == self.front):
            return False
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
            return True
        else:
            self.rear = (self.rear + 1)%self.n
            self.queue[self.rear] = value
            return True

    # Dequeues pop element from queue. Returns -1 if the queue is empty, otherwise returns the popped element.
    def dequeue(self):
        # Write your code here.
        if (self.front == -1):
            return -1
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1)%self.n
            return temp

