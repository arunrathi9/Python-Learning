#leetcode problem

def peakIndexInMountainArray(arr):
        s=0;e=len(arr)-1;
        mid = s + (e-s)//2
        while(s<e):
            if arr[mid] < arr[mid+1]:
                s = mid + 1
            else:
                e = mid

            mid = s + (e-s)//2

        return e

arr = [1,5,10,5,2]
print(peakIndexInMountainArray(arr))