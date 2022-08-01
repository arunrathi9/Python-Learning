# Coding Ninjas problem

def reverse(arr):
    i = 0; j = len(arr)-1
    while(i<j):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i += 1
        j -= 1
    
    return arr

def findArraySum(a, n, b, m):
    # Write your code here.
    i = n-1; j = m-1
    carry = 0
    ans = []
    while(i>=0 and j>=0):
        sum_ = a[i] + b[j] + carry
        carry = sum_//10
        sum_ = sum_ % 10
        ans.append(sum_)
        i -=1; j-=1
    
    while(i>=0):
        sum_ = a[i] + carry
        carry = sum_//10
        sum_ = sum_ % 10
        ans.append(sum_)
        i -= 1

    while(j>=0):
        sum_ = b[j] + carry
        carry = sum_//10
        sum_ = sum_ % 10
        ans.append(sum_)
        j -= 1
    
    while(carry!=0):
        sum_ = carry
        carry = sum_//10
        sum_ = sum_ % 10
        ans.append(sum_)


    return reverse(ans)

print(findArraySum([4,5,1], 3, [3,4,5], 3))
print(findArraySum([1,2,3,4], 4, [6], 1))
print(findArraySum([1,2,3], 3, [9,9], 2))
print(findArraySum([9,9,9], 3, [9,9,9], 3))