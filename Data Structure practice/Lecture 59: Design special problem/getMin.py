# coding ninjas - Design a Stack that supports getMin() in O(1) time
# & O(1) extra space

class SpecialStack:
    # Define the data members.
    s = []
    mini = 10**9+1

    '''----------------- Public Functions of SpecialStack ----------------'''

    def push(self,data):
        if len(self.s) == 0:
            self.s.append(data)
            self.mini = data
        else:
            if data<self.mini:
                val = 2*data - self.mini
                self.s.append(val)
                self.mini = data
            else:
                self.s.append(data)
    
    def pop(self):
        if len(self.s) == 0:
            return -1
        
        curr = self.s[-1]
        self.s.pop()
        
        if curr > self.mini:
            return curr
        else:
            prevMin = self.mini
            val = 2*self.mini - curr
            self.mini = val
            return prevMin

    def top(self):
        if self.isEmpty():
            return -1
        
        curr = self.s[-1]
        if curr < self.mini:
            return self.mini
        else:
            return curr
            

    def isEmpty(self):
        return True if len(self.s) == 0 else False

    def getMin(self):
        if self.isEmpty():
            return -1
        return self.mini

s = SpecialStack()

s.push(13)
s.push(47)

print(s.getMin())
print(s.isEmpty())
print(s.pop())
print(s.top())
