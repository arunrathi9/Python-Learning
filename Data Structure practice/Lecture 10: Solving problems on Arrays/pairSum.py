# coding ninjas

def pairSum(arr, s):
    ans = []
    n = len(arr)
    for i in range(n):
        temp = s-arr[i]
        for j in range(i+1, n):
            if temp == arr[j]:
                if arr[i]<arr[j]:
                    ans.append([arr[i], arr[j]])
                else:
                    ans.append([arr[j], arr[i]])

    return sorted(ans, key=lambda x:x[0])

arr = [2, -3, 3, 3, -2]
print(pairSum(arr, 0)) 
