# Coding Ninja problem - Reverse Words In A String

def reverse(arr):
    i=0;j=len(arr)-1
    while(i<=j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i+=1
        j-=1
    
    return arr

def reverseString(str):
	#Write your code here.
    res = " ".join(reverse(str.split()))
    return res

print(reverseString("Welcome to Coding Ninjas"))
print(reverseString("I love    coding"))
print(reverseString(" Hey   There!!"))