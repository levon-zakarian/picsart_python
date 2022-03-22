"""
f ֆունկցիան սահմանվում է հետևայլ կերպ.
f(n) = n, եթե n < 3
f(n) = f(n - 1) + f(n - 2) + f(n - 3), եթե n >= 3
n-ը կարող է լինել միայն 0 և դրական ամբողջ թիվ։ Իրականացրեք լուծումը
ռեկուրսիվ, իտերատիվ և պոչավոր ռեկուրսիվ տարբերակներով։
"""

# Ռեկուրսիվ լուծում
def func_1(n):
    if n < 3:
        return n
    return func_1(n - 1) + func_1(n - 2) + func_1(n - 3)

    # return n if n < 3 else func_1(n - 1) + func_1(n - 2) + func_1(n - 3) # Տեռռար օպերատորով


# Իտերատիվ լուծում
def func_2(n):
    a = 0
    b = 1
    c = 2

    while n > 0:
        tmp = a + b + c
        a = b
        b = c
        c = tmp
        n -= 1
    return a


# Պոչավոր ռեկուրսիվ լուծում ֆունկցիայի կանչը՝ func_3 (n, 0, 1, 2)
def func_3(n, a, b, c):
    if n == 0:
        return a
    return func_3(n - 1, b, c, a + b + c)

    # return a if n == 0 else func_3(n - 1, b, c, a + b + c) # Տեռռար օպերատորով


print(func_1(2))
print(func_1(3))
print(func_1(4))
print(func_1(5))
print(func_1(6))
print(func_1(7))

print(func_2(2))
print(func_2(3))
print(func_2(4))
print(func_2(5))
print(func_2(6))
print(func_2(7))

print(func_3(2, 0, 1, 2))
print(func_3(3, 0, 1, 2))
print(func_3(4, 0, 1, 2))
print(func_3(5, 0, 1, 2))
print(func_3(6, 0, 1, 2))
print(func_3(7, 0, 1, 2))
