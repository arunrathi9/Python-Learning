# SPOJ Problem:

def isPossible(arr, n, k, mid):
    runningSum = 0
    for i in range(n):
        if arr[i]>mid:
            runningSum += arr[i]-mid
            if runningSum >= k:
                return True
    
    return False

def eko(arr, k):
    s = min(arr)
    e = max(arr)
    mid = s + (e-s)//2
    ans = -1

    #arr = sorted(arr)

    while(s<=e):
        if isPossible(arr, len(arr), k, mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
        mid = s + (e-s)//2

    return ans

print(eko([20,15,10,17], 7))
print(eko([4,42,40,26,46], 20))