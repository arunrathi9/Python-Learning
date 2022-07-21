# Coding Ninjas Problem - Cooking Ninjas

def minCookTime(rank, m):
    e = 5*m*(m+1)
    s = 1
    mid = s + (e-s)//2

    while(s<e):
        dishCooked = 0
        for i in range(len(rank)):
            timeRemain = mid
            dishCount = 0
            while(timeRemain>0):
                timeRemain -= (dishCount+1)*rank[i]
                if timeRemain >= 0:
                    dishCount += 1
            dishCooked += dishCount
        if dishCooked < m:
            s = mid + 1
        else:
            e = mid
        mid = s + (e-s)//2
    return mid
        
print(minCookTime([10], 1))
print(minCookTime([1,2,3,4], 11))
print(minCookTime([1,1,1,1,1,1,1,1], 8))