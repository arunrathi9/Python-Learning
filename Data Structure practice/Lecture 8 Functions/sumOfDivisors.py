# GFG - Sum of all divisors from 1 to n


def numDivisors(k):
    sum = 0
    for i in range(1, int(k**0.5)+1):
        if k%i==0:
            sum += i
            if (k//i != i):
                sum += k//i
    return sum
    
def sumOfDivisors(N):
    #code here
    sum_ = 0
    for i in range(1,N+1):
        # method 1 - brute force
        # sum_ += numDivisors(i)
        sum_ += (N//i)*i

    return sum_
        

print(sumOfDivisors(1000000))