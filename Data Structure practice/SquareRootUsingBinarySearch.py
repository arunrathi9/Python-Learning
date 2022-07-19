def squareRoot(n):
    s = 0; e = n;
    ans = -1
    mid = s + (e-s)//2
    while(s<=e):
        prod = mid*mid
        if prod == n:
            return mid
        elif prod > n:
            e = mid - 1
        elif prod < n:
            ans = mid
            s = mid + 1
        mid = s + (e-s)//2
    
    return ans

print(squareRoot(24))