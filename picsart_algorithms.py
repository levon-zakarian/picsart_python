from datetime import date, datetime

date_str = '2021-12-14'

dto = datetime.strptime(date_str, '%Y-%m-%d').date()
print(type(dto))
print(dto)



today = date.today()
print("Today's date:", today)
"""
def makeres(lst):
    maximum = 0
    for i in range(len(lst) - 1):
        for j in range(i, len(lst)):
            mak = min(lst[i],lst[j]) * (j - i)
            if mak > maximum:
                maximum = mak

    return maximum

test_1 = [10, 1, 9, 3, 4]
test_2 = [5, 8, 3, 9, 5]
print(makeres(test_1))
print(makeres(test_2))

def water(lst):
    amount = 0
    gap = 0
    i = 0
    broken = 0
    while i <= len(lst) - 1:
        for j in range(i + 1, len(lst)):
            if lst[j] >= lst[i]:
                amount = amount + gap
                gap = 0
                i = j
                broken = 1
                break
            else:
                gap = gap + lst[i] - lst[j]
                if j == len(lst) - 1:
                    gap = 0
        if broken == 1:
            broken = 0
            continue
        i = i + 1
    return amount

A = [4,2,0,3,2,5]
B = [0,1,0,2,1,0,1,3,2,1,2,1]
C = [1, 0, 4, 2, 3, 2, 4, 2, 6]

print("Output A: " + str(water(A)))
print("Output B: " + str(water(B)))
print("Output B: " + str(water(C)))

"""