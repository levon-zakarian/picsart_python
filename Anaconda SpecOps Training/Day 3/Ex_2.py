"""
Տրված է անուններ պարունակող ֆայլը (https://projecteuler.net/project/resources/p022_names.txt),
արտագրել արժեքները մեկ այլ ֆայլում, որտեղ մեծատառով կլինեն միայն անունների առաջին տառերը։
"""

from urllib.request import urlopen

with open("Capitalized_names.txt", "w") as file:
    for line in urlopen("https://projecteuler.net/project/resources/p022_names.txt"):
        file.write(line.decode("utf-8").title())
