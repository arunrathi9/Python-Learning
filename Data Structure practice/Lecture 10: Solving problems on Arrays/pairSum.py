# coding ninjas

def pairSum(arr, s):
    # ans = []
    # n = len(arr)
    # for i in range(n):
    #     temp = s-arr[i]
    #     for j in range(i+1, n):
    #         if temp == arr[j]:
    #             if arr[i]<arr[j]:
    #                 ans.append([arr[i], arr[j]])
    #             else:
    #                 ans.append([arr[j], arr[i]])

    # return sorted(ans, key=lambda x:x[0])

    # method 2 - using Hashing
    ans = []
    ht = {}
    for i in range(len(arr)):
        temp = s-arr[i]
        if temp in ht:
            for _ in range(ht[temp]):
                if temp<arr[i]:
                    ans.append([temp, arr[i]])
                else:
                    ans.append([arr[i], temp])
        if arr[i] in ht:
            ht[arr[i]] += 1
        else:
            ht[arr[i]] = 1
    
    return sorted(ans, key=lambda x: x[0])

#arr = [2, -3, 3, 3, -2]; s =0
arr = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7,-8,-9]
print(pairSum(arr, 10)) 
