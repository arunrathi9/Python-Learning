#Leetcode problem

def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [0]*n
        for i in range(n):
            res[(i+k)%n] = nums[i]

        #nums[:] = res
        return res

print(rotate([-1,-100,3,99], 2))