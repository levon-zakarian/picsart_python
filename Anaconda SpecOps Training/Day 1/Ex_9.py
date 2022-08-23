"""
Հաշվել տրված թվի թվանշանների արտադրյալի և գումարի տարբերությունը։
Օրինակ, տրված է 4637, վերադարձնել (4*6*3*7) - (4+6+3+7):
"""

given_number = 4637
sum = 0
prod = 1

while given_number > 0:
    sum += given_number % 10
    prod *= given_number % 10
    given_number //= 10

print(prod - sum)
