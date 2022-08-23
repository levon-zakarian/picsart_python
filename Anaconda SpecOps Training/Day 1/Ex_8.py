"""Հաշվել տրված թվի թվանշանների գումարը։ Օրինակ, տրված է 4637, վերադարձնել 4+6+3+7:"""

given_number = 4637
sum = 0

while given_number > 0:
    sum += given_number % 10
    given_number //= 10

print(sum)
