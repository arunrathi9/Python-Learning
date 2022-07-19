# Coding Ninjas - Importance *****

def isPossible(arr, n, m, mid):
    pageSum = 0
    studentCount = 1
    for i in range(n):
        if (pageSum + arr[i]) <= mid:
            pageSum += arr[i]
        else:
            studentCount += 1
            if (studentCount > m or arr[i]>mid):
                return False
            pageSum = arr[i]
    
    return True
    

def allocateBooks(arr, n, m):

    sum_ = sum(arr)

    s = 0; e = sum_; ans = -1
    mid = s + (e-s)//2

    while(s<=e):

        if isPossible(arr, n, m, mid):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

        mid = s + (e-s)//2

    return ans

print(allocateBooks([10,20,30,40], 4, 2))
print(allocateBooks([25, 46, 28, 49, 24], 5, 4))