"""
Գրել ծրագիր, որը կհաշվի տրված զանգվածի արժեքների քառակուսիները և կպահի դրանք
նոր զանգվածում՝ սորտավորված ձևով։
"""

my_array = [1, 4, 6, 7, 8, 3, 5, 2, 9, 3, 14, 16, 12, 15, 19, 38, 74, 51, 24, 96, 13]
square_array = []

for number in my_array:
    square_array.append(number**2)
square_array.sort()
print(square_array)
