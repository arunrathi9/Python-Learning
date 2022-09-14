# Leetcode problem - Complement of Base 10 int

def bitwiseComplement(n: int) -> int:
    m = n
    mask = 0
    if n == 0:
        return 1
    while(m):
        mask = mask<<1 | 1
        m = m >> 1

    return ~n & mask

print(bitwiseComplement(5))
print(bitwiseComplement(10))