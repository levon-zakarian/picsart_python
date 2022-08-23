"""Իրականացնել ծրագիր, որը կհաշվի թե յուրաքանչյուր բառ քանի անգամ է հանդիպում տեքստային ֆայլում։"""

with open("Achq_u_Luys.txt", "r") as file:
    words_counts = {}
    for line in file:
        for word in line.split():
            for char in word:
                if not char.isalnum():
                    word = word.replace(char, "")
            if words_counts.get(word):
                words_counts[word] += 1
            else:
                words_counts[word] = 1
    print(words_counts)
