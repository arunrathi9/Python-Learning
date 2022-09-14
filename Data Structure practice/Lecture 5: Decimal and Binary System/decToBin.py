# Decimal to Binary

def decToBin(n):
    ans = 0
    i = 0
    while(n>0):
        bit = n & 1
        ans = bit*(10**i) + ans
        n = n>>1
        i += 1
    
    return ans

print(decToBin(5))

def decToBinNegative(n):
    ans = 0
    i = 0
    n = abs(n)
    while(n>0):
        bit = n & 1
        ans = bit*(10**i) + ans
        n = n >> 1
        i += 1
    
    print("bin of n: ", ans)
    ans = ~ans
    print("1's comp: ", ans)
    ans += 1
    print("2's comp: ", ans)

    return ans

print(decToBinNegative(-6))