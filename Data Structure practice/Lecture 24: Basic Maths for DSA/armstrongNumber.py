# GFG problem - check armstrong number

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        ans = 0
        temp = n
        while(temp):
            digit = temp%10
            ans += digit**3
            temp //= 10
        return "Yes" if ans == n else "No"

if __name__ == "__main__":
    num = int(input("Enter number:"))
    print(Solution().armstrongNumber(num))