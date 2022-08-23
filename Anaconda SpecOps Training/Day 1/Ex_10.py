"""
Գրել ֆունկցիա, որը ստանում է միջակայքի սկիզբ և վերջ (երկու թվեր) և հաշվում միջակայքում
գտնվող կենտ թվերի քանակը։ Օրինակ, 3 և 7 միջակայքում կա երեք կենտ թիվ (3, 5, 7):
"""


def numberOfOdds(start, end):
    count = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            count += 1
    return count


print(numberOfOdds(3, 7))
print(numberOfOdds(1, 10))
