"""
Իրականացրեք fast_pow-ն իտերատիվ տարբերակով։Իրականացրեք fast_pow-ն իտերատիվ տարբերակով։
"""

# Թվի կենտության ստուգման ֆունկցիա
def is_odd(n):
    return n % 2 != 0

# Թվի քառակուսի բարձրացման ֆունկցիա
def square(n):
    return n ** 2


# m ^ n ֆունկցիա իտերատիվ տարբերակով
def fast_pow_iter(m, n):
    res = 1
    while n > 0:
        if is_odd(n):
            res *= m
            n -= 1
        m = square(m)
        n /= 2
    return res

a = 2
b = 12

for k in range(b + 1):
    print(f"Func of {k}: {fast_pow_iter(a,k)}")
    print(f"Built-in of {k}: {a**k}")
    print("------------------------")
