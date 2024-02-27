
# AND
n = 1 & 1
# OR
n = 1 | 0
# XOR
n = 0 ^ 1
# NOT (negation)
n = ~n
# Bit shifting
n = 1
n = n << 1 # multiply 2
n = n >>1 # multiply 1/2

# Counting Bits
def countBits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1 # same as n // 2
    return count


if __name__=="__main__":
    print(countBits(23))