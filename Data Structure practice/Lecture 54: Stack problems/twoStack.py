#coding ninjas problem - two stacks

class TwoStack:
    
    def __init__(self, s):
        self.size = s
        self.arr = [0]*s
        self.top1 = -1
        self.top2 = s
     
    # Push function for the first stack
    def push1(self, val):
        if (self.top2-self.top1)>1:
            self.top1 += 1
            #print(self.top1)
            self.arr[self.top1] = val
      
    # Push function for the second stack
    def push2(self, val):
        if (self.top2-self.top1)>1:
            self.top2 -= 1
            #print(self.top2)
            self.arr[self.top2] = val
            
        
    # Pop function for the first stack
    def pop1(self):
        if self.top1>=0:
            #print(self.top1)
            val = self.arr[self.top1]
            self.top1 -= 1
            return val
        else:
            return -1
        
    # Pop function for the second stack
    def pop2(self):
        if self.top2<self.size:
            val = self.arr[self.top2]
            self.top2 += 1
            return val
        else:
            return -1

t2 = TwoStack(3)
# For more, check the coding ninjas problem statement