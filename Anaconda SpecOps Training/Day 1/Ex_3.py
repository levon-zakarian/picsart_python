"""Օգտագործելով աղյուսակ (dictionary) հաշվել զանգվածում բոլոր թվերի կրկնությունների քանակը։"""

my_array = [1, 2, 4, 5, 3, 4, 1, 2, 1, 2, 1, 3, 4, 5, 7, 8, 9]

my_dict = {}

for number in my_array:
    if my_dict.get(number):
        my_dict[number] += 1
    else:
        my_dict[number] = 1

print(my_dict)
