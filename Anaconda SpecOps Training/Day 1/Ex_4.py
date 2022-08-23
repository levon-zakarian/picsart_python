"""
Տեքստային ֆայլի համար իրականացնել ծրագիր, որը կհաշվի ֆայլում հանդիպող սիմվոլների քանակը
"""


with open("Lorem_ipsum.txt", "r") as file:
    number_of_symbols = 0
    num_of_chars = 0
    for character in file.read():
        if character not in (" ", "\n"):
            num_of_chars += 1
        if not character.isalnum():
            number_of_symbols += 1
    print(
        f"Ֆայլում առկա բոլոր սիմվոլների քանակը բացի նոր տողից և բացատից - {num_of_chars}"
    )

    print(
        f"Ֆայլում առկա նշանների քանակը (բացատ, ՛ ' \", նոր տող) - {number_of_symbols}"
    )
