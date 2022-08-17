# Coding ninja problem - Subsequence of a String

def subsequence(arr, res, output, index):

    if index>=len(arr):
        if len(output) != 0:
            res.append(output)
        return
    
    subsequence(arr, res, output, index+1)

    output += arr[index]
    subsequence(arr, res, output, index+1)
    output = output.replace(arr[index], "")


arr = "abc"
res = []
output = ""
subsequence(arr, res, output, 0)
print(res)