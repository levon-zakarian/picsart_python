"""
Իրականացնել pow(a, b) ֆունկցիան՝ հաշվի առնելով, որ b-ն կարող է լինել նաև ոչ դրական։
Հիշեցնենք`
a ** b = a ** b, եթե a > 0
a ** b = (1 / a ** (-b)), եթե b < 0
a ** b = 1, եթե b = 0
Նաև հաշվի առեք, որ a-ի b աստիճանը սխալ արտահայտություն է, եթե a-ն հավասար է 0, իսկ b-ն բացասական է
"""

def pow (a, b):
    res = 1
    count = 0
    if b >= 0:
        while count < b:
            res = res * a
            count = count + 1
    else:
        if a == 0:
            return "Wrong equation"
        while count < -b:
            res = res * (1 / a)
            count = count + 1
    return res

print(pow(3,4))
print(pow(-5,2))
print(pow(-6,3))
print(pow(2,-3))
print(pow(412,0))
print(pow(0,41))
print(pow(0,-4))