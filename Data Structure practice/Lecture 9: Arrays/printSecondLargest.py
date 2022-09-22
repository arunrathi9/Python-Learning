# GFG - Second largest number in an array

class Solution:

    def print2largest(self,arr, n):
        # code here
        first_largest = -1
        second_largest = -1
        for i in range(n):
            if arr[i]>first_largest:
                first_largest = arr[i]
        
        for i in range(n):
            if arr[i]>second_largest and arr[i] < first_largest:
                second_largest = arr[i]
        
        return second_largest

arr = [1]
print(Solution().print2largest(arr, len(arr)))