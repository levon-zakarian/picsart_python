"""
Ստեղծեք ֆունկցիա, որը որպես արգումենտ ստանում է երեք թվեր և վերադարձնում է դրանցից երկու
մեծագույնների քառակուսիների գումարը։
"""
def biggest_square(a, b, c):
    #   a-ն մեծագույնն է
    if a >= b and a >= c:
        biggest_1 = a
        #   Երկրորդ մեծագույնի հաշվում
        if b >= c:
            biggest_2 = b
        else:
            biggest_2 = c
    #   b-ն մեծագույնն է
    elif b >= a and b >= c:
        biggest_1 = b
        #   Երկրորդ մեծագույնի հաշվում
        if a >= c:
            biggest_2 = a
        else:
            biggest_2 = c
    #   c-ն մեծագույնն է
    else:
        biggest_1 = c
        #   Երկրորդ մեծագույնի հաշվում
        if a >= b:
            biggest_2 = a
        else:
            biggest_2 = b

    #   Մեշագույնների քառակուսի բարձրացում և գումարում
    return biggest_1**2 + biggest_2**2

print(biggest_square(3, 4, 5))
print(biggest_square(2, 3, 1))
print(biggest_square(4, 3, 2))
