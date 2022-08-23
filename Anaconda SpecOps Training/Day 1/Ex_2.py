"""
Տրված ֆայլում պարունակվում է տեքստ։ Իրականացնել ծրագիր, որը ֆայլի մեջ պարունակվող տեքստի բոլոր
բառերի առաջին տառերը դարձնում է մեծատառ և ձևափոխված ամբողջ տեքստը պահպանում մեկ այլ ֆայլում։
"""

with open("Lorem_ipsum.txt", "r") as file:
    with open("Lorem_ipsum_capitalized.txt", "w") as new_file:
        for line in file:
            new_file.write(line.title())
