# Leetcode problem - Unique number of Occurences
from collections import Counter

def uniqueOccurrences(arr):
    count_arr = list(Counter(arr).values())
    n = len(count_arr)
    for i in range(n):
        if count_arr[i] in count_arr[i+1:]:
            return False
    return True
    
arr = [1,2,2,1,1,3]
arr = [1]
print(uniqueOccurrences(arr))