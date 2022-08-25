"""
Իրականացնել strmove() ֆունկցիան, որը տրված տողը ցիկլիկ տեղաշարժում է դեպի աջ տրված քանակով։
Օրինակ, strmove(“hello”, 2); կտեղաշարժի “hello”-ն 2 դիրքով դեպի աջ և կստանա “lohel”:
"""

my_string = "Hello"


def strMove(string, shift):
    return string[len(string) - shift :] + string[: len(string) - shift]


print(strMove(my_string, 2))
print(strMove("Lorem ipsum dolor", 4))
