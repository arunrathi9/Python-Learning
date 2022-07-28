# LeetCode: merge sorted array

def mergeSortedArray(nums1,m,nums2,n):
    # i,j = 0,0
    # res = []
    # while(i<m and j<n):
    #     if nums1[i] < nums2[j]:
    #         res.append(nums1[i])
    #         i += 1
    #     elif nums1[i] == nums2[j]:
    #         res.append(nums1[i])
    #         res.append(nums2[j])
    #         i += 1
    #         j += 1
    #     else:
    #         res.append(nums2[j])
    #         j += 1

    # while(i<m):
    #     res.append(nums1[i])
    #     i += 1
    
    # while(j<n):
    #     res.append(nums2[j])
    #     j += 1

    # nums1 = res
    # return nums1
    #method 2
    if n != 0 and (n!=1 or m!=0):
        i,j = 0,0
        while(i<n+m and j<n):
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
            # elif nums1[i] == 0:
            #     nums1[i] = nums2[j]
            #     j += 1
            i += 1
        for i in range(m+n,0,-1):
            if nums1[i-1] != 0:
                break
        
        while(j<n):
            nums1.insert(i, nums2[j])
            nums1.pop()
            j += 1
            i += 1
    if n == 1 and m==0:
        nums1[0] = nums2[0]
    
    return nums1

nums1 = [2,0]; m = 1; nums2 = [1]; n = 1
#nums1 = [0]; m = 0; nums2 = [1]; n = 1
#nums1 = [4,5,6,0,0,0]; m = 3; nums2 = [1,2,3]; n = 3
#nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
#nums1 = [-1,0,0,3,3,3,0,0,0]; m = 6; nums2=[1,2,2]; n=3
print(mergeSortedArray(nums1, m, nums2, n))