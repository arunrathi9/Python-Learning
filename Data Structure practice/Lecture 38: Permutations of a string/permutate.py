# Leetcode problem - Permutation of a String

def permutate(str, index, res):

    if index>=len(str):
        res.append(str.copy())
        return

    for j in range(index, len(str)):
        str[index], str[j] = str[j], str[index]
        permutate(str, index+1, res)
        #backtrack
        str[index], str[j] = str[j], str[index]
        


str = ['a', 'b', 'c']
res = []
permutate(str, 0, res)
print(res)