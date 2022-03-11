"""
Ստեղծել ֆունկցիա, որը ստանում է երկու թվային արգումենտ` a և b, և վերադարձնում է a-ից մինչև b
ընկած ամբողջ թվերի գումարը։ Կարող եք ենթադրել, որ առաջին արգումենտը միշտ փոքր է երկրորդից։
"""

def mijakayq (a, b):
    result = 0
    counter = a
    while counter < b:
        result += counter
        counter += 1
    return result

print(mijakayq(0,5))
print(mijakayq(1,5))
print(mijakayq(41,46))

