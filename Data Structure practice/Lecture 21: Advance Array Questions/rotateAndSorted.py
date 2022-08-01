# LeetCode problem

def check(nums):
        n = len(nums)
        count = 0
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                count += 1
            
        if nums[n-1] > nums[0]:
            count += 1
        
        return count <= 1

print(check([3,4,5,1,2]))
print(check([3,5,7,1,6]))