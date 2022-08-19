# Leetcode problem - Letter Combinations of a Phone Number

def letterCombinations(digits, output, res, index):

    if index >= len(digits):
        res.append(output)
        return

    number = ord(digits[index]) - ord('0')
    for val in mapping[number]:
        output += val
        letterCombinations(digits, output, res, index+1)
        idx = output.rfind(val)
        output = output[:idx] + output[idx+1:]
    

mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
digits = '2'
res = []
output = ""
index = 0
letterCombinations(digits, output, res, index)
print(res)

digits = '22'
res = []
output = ""
index = 0
letterCombinations(digits, output, res, index)
print(res)