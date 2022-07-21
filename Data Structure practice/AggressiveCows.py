# Coding Ninjas

def isPossible(stalls, n, k, mid):
    lastpos = stalls[0]
    cowCount = 1
    for i in range(n):
        if (stalls[i]-lastpos) >= mid:
            cowCount += 1
            if cowCount == k:
                return True
            lastpos = stalls[i]
    return False

def aggressiveCows(stalls, k):
    stalls = sorted(stalls)

    s = 0 
    e = stalls[-1] - stalls[0]

    mid = s + (e-s)//2
    while(s<=e):
        if isPossible(stalls, len(stalls), k, mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
        mid = s + (e-s)//2
    return ans

print(aggressiveCows([87, 93, 51, 81, 68, 99, 59], 4))