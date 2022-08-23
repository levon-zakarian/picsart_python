"""
Տրված ֆայլում պարունակվում են թվեր։ Իրականացնել ծրագիր, որը հաշվում և վերադարձնում է ֆայլում
պարունակվող թվերի գումարը։
"""

with open("Numbers.txt", "r") as file:
    sum = 0
    for line in file:
        try:
            sum += int(line)
        except:
            sum += 0
    print(sum)
