"""
Գրել ծրագիր, որը հաշվում է 1-ից 100 թվերի գումարի քառակուսին (1+...+100)^2, հաշվում է 1-ից 100
թվերի քառակուսիների գումարը՝ (1^2 + 2^2 + … + 100^2): Ծրագիրը տպում է ստացված թվերի տարբերությունը։
"""

sum_square = 0
squares_sum = 0

for i in range(1, 101):
    sum_square += i
    squares_sum += i**2
sum_square = sum_square**2

print(sum_square - squares_sum)
