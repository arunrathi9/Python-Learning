# leetcode - count primes

# TC - O(n*(log(log(n))))
# using sieve of eratosthenes

def countPrimes(n):

    arr = [True]*(n+1)

    arr[0] = arr[1] = False
    count = 0
    for i in range(2, n):
        if arr[i]:
            count += 1
            for j in range(2*i,n, i):
                arr[j] = False
    
    return count

print(countPrimes(40))