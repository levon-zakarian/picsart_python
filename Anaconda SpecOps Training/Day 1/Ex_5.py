"""Իրականացնել ֆունկցիա, որը կհեռացնի ստացված տողի (string) ամեն երրորդ սիմվոլը։"""

my_line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
example = "123123123123123123123123123123123123123"


def removeEveryThird(line):
    new_string = ""
    for index, character in enumerate(line):
        if not (index + 1) % 3 == 0:
            new_string += character
    return new_string

    # Այլ տարբերակ բայց մի տեսակ շատ դաժան կլինի մի 200 անդամանոց լիստ սարքելը
    # new_string = list(line)
    # del new_string[2::3]
    # new_string = "".join(new_string)
    # print(new_string)


print(removeEveryThird(my_line))
print(removeEveryThird(example))
