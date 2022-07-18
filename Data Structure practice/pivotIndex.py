# # leetcode problem
# # pivot index = index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# def pivot(arr, n):
#     s = 0; e = n-1
#     ans = -1
#     mid = s + (e-s)//2
#     l_sum = 0
#     r_sum = 0
#     while(s<=e):
#         if mid < n:
#             l_sum = sum(arr[:mid])
#             r_sum = sum(arr[mid+1:])
        
#         if l_sum == r_sum:
#             ans = mid
#             e = mid - 1
#         elif l_sum<r_sum:
#             s = mid + 1
#         elif l_sum>r_sum:
#             e = mid - 1
        
#         mid = s + (e-s)//2

#     return ans

# arr = [1,7,3,6,5,6]
# print(pivot(arr, len(arr)))

# arr = [1,2,3]
# print(pivot(arr, len(arr)))

# arr = [-1,-1,-1,-1,0,1]
# print(pivot(arr, len(arr)))

def pivot(arr):
    s = 0; e = len(arr)-1
    mid = s + (e-s)//2
    while(s<e):
        if arr[mid] >= arr[0]:
            s = mid + 1
        else:
            end = mid

        mid = s + (e-s)//2

    return s

arr = [3,8,10,17,1]
print(pivot(arr))