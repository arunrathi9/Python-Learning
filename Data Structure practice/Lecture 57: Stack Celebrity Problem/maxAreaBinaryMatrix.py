class Solution:
    def nextSmallerElement(self, arr, n):
        stack = [-1]
        ans = [0] * n
        
        for i in range(n-1, -1, -1):
            while(stack[-1] != -1 and arr[stack[-1]]>=arr[i]):
                stack.pop()
            
            ans[i] = stack[-1]
            stack.append(i)
            
        return ans
        
    def prevSmallerElement(self, arr, n):
        
        stack = [-1]
        ans = [-1]*n

        for i in range(n):
            curr = arr[i]
            while(stack[-1] != -1 and arr[stack[-1]] >= curr):
                stack.pop()

            if stack[-1] != -1:
                ans[i] = stack[-1]
            stack.append(i)
        
        return ans
            
                

    def largestRectangle(self, arr, m):
        
        ##n = len(arr)
        
        next = self.nextSmallerElement(arr, m)
        
        prev = self.prevSmallerElement(arr, m)
        
        area = -1
        for i in range(m):
            l = arr[i]
            if (next[i] == -1):
                next[i] = m
            b = next[i] - prev[i] - 1 
            new_area = l * b
            area = new_area if new_area > area else area
            
        return area
    
    def maxArea(self, M, n, m):
        
        area = self.largestRectangle(M[0], m)

        for i in range(1, n):
            for j in range(m):
                if M[i][j] != 0:
                    M[i][j] += M[i-1][j]
                else:
                    M[i][j] = 0

            newArea = self.largestRectangle(M[i], m)
            area = newArea if newArea > area else area
        
        return area

s = Solution()
M = [[0,1,1,0], [1,1,1,1], [1,1,1,1], [1,1,0,0]]
print(s.maxArea(M, len(M), len(M[0])))