# coding ninjas problem - N stack in an array

class NStack:
    def __init__(self, n, s):
        
        self.free_spot = 0
        self.top = [-1]*n
        self.next = []
        self.arr = [0]*s
        
        for i in range(len(self.arr)-1):
            self.next.append(i+1)
            
        self.next.append(-1)    

    # Pushes 'X' into the Mth stack. Returns true if it gets pushed into the stack, and false otherwise.
    def push(self, x, m):
        
        if (self.free_spot == -1):
            return False
        # find index of free spot
        index = self.free_spot
        
        # update freespot
        self.free_spot = self.next[index]
        
        # insert in an array
        self.arr[index] = x
        
        # update next
        self.next[index] = self.top[m-1]
        
        # update top
        self.top[m-1] = index  
        
        return True
    # Pops top element from Mth Stack. Returns -1 if the stack is empty, otherwise returns the popped element.
    def pop(self, m):
        
        if (self.top[m-1] == -1):
            return -1
        
        index = self.top[m-1]
        
        self.top[m-1] = self.next[index]
        
        self.next[index] = self.free_spot
        
        self.free_spot = index
        
        return self.arr[index]

s = NStack(3, 6)
s.push(10, 1)
s.push(20,1)
s.push(30,2)
print(s.pop(1))
print(s.pop(2))