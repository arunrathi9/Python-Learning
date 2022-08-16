# reverse the string using recursion

def reverse(arr, i, j):

    if (i>j):
        return

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    i += 1
    j -= 1

    reverse(arr, i, j)

arr = 'Welcome to Coding Ninjas'.split()
reverse(arr, 0, 3)
print(" ".join(arr))