# Leetcode - move zeroes
def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        if len(nums) == 1:
            return nums
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = 0
                nums[non_zero] = temp
                non_zero += 1
        return nums

print(moveZeroes([0,1,0,3,12]))