"""
Նյուտոնի մեթոդը խորանարդ արմատ հաշվելու համար հիմնված է հետևյալ քայլերի վրա.
եթե n-ը m թվի մոտարկված արմատն է, ապա մենք կարող ենք էլ ավելի բարելավել մոտարկումը հետևայլ քայլով
((m / (n ** 2)) + (2 * n)) / 3
Այս բանաձևով ստեղծեք ֆունկցիա, որը հաշվում է թվի խորանարդ արմատը։
"""
def cube_root(n):
    root = 1
    while not guess_enough(root, n, 0.0001):
        root = improve(root, n)
    return root

def guess_enough(value, target, approx):
    return abs(value ** 3 - target) < approx

def abs(n):
    if n > 0:
        return n
    return -n

def improve(root, target):
    return ((target / (root ** 2)) + (2 * root)) / 3

print(cube_root(27))
print(cube_root(15))
print(cube_root(9))
print(cube_root(-64))
print(cube_root(-125))
print(cube_root(729))
print(cube_root(-729))
print(cube_root(143))
