# GCd and LCM using euclid algorithm

class Solution:
    
    def findGcd(self, a, b):
        # using recursion
        # if b == 0:
        #     return b
        # else:
        #     return self.findGcd(b, a%b)

        # method 2
        while(b):
            a, b = b, a%b
        return a
            
        
    def lcmAndGcd(self, A , B):
        # code here
        if A>B:
            gcd = self.findGcd(A, B)
        else:
            gcd = self.findGcd(B, A)
        lcm = (A*B)//gcd
        return lcm, gcd

a,b = 113094, 9449384
print(Solution().lcmAndGcd(a, b))