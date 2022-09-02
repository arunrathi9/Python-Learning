# coding ninjas - queue

class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.queue = []

    '''----------------- Public Functions of Queue -----------------'''

   
    def isEmpty(self) :
        #Implement the isEmpty() function
        return True if len(self.queue) == 0 else False
    

    def enqueue(self, data) :
        #Implement the enqueue(element) function
        self.queue.insert(0, data)
        #print(self.queue)


    def dequeue(self) :
        #Implement the dequeue() function
        return -1 if self.isEmpty() else self.queue.pop()



    def front(self) :
        #Implement the front() function
        return -1 if self.isEmpty() else self.queue[-1]