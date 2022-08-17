# leetcode - subsets


def subsets(arr, index, output, res):
    
    if index>=len(arr):
        res.append(output.copy())
        return

    subsets(arr, index+1, output, res)

    element = arr[index]
    output.append(element)
    subsets(arr, index+1, output, res)
    output.remove(element)

arr = [1,2,3]
index = 0
res = []
output = []
subsets(arr, index, output, res)
print(res)