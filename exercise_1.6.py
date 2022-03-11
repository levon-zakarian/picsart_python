"""
Իրականացնել նախորդ վարժությունում տրված ֆունկցիան՝ հաշվի առնելով, որ առաջին արգումենտը կարող է
մեծ լինել երկրորդից։ Այդ դեպքում ֆունկցիան պետք է վերադարձնի b-ից մինչև a ամբողջ թվերի գումարը։
"""

def mijakayq (a, b):
    result = 0
    if b >= a:
        counter = a
        limit = b
    else:
        counter = b
        limit = a
    while counter < limit:
        result += counter
        counter += 1
    return result

print(mijakayq(5,0))
print(mijakayq(1,5))
print(mijakayq(46,41))