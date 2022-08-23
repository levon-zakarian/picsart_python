print("----------------------------------")
data = [1, 2, 3, 4]


def contain(data, val):
    """Վերադարձնում է boolean արժեք True եթե val-ը գտնվում է data-ի մեջ"""
    return val in data


value_1 = 3
value_2 = 8
print("contain(data, 3)")
print(f"{data}-ի մեջ {value_1} {'կա' if contain(data, value_1) else 'չկա'}")
print("contain(data, 8)")
print(f"{data}-ի մեջ {value_2} {'կա' if contain(data, value_2) else 'չկա'}")
print("----------------------------------")


data_2 = [0, 1, 2, 3]


def pop(data, i=None):
    """data-ից հանում է i-երորդ անդամը, եթե i տրված չէ, ապա հանում է վերջինը"""
    if i:
        new_data = data[:i]
        for number in data[i + 1 :]:
            new_data.append(number)
        return new_data
    return data[:-1:]
    # data.pop(i) if i else data.pop()


print(f"data = {data_2}")
print("pop(data, 2)")
print(pop(data_2, 2))
print("pop(data)")
print(pop(data_2))
print("----------------------------------")


def remove_all(data, value):
    """Data-ից հեռացնում է բոլոր անդամները որոնց արժեքը value է"""
    while contain(data, value):
        data.remove(value)
    return data


data_3 = [1, 2, 3, 4, 2]

print(f"data = {data_3}")
print("remove_all(data, 2)")
print(remove_all(data_3, 2))
print("----------------------------------")


def reverse(data):
    """Շրջում է data-ն"""
    data = data[::-1]
    return data
    # data = data.reverse()


data_4 = [1, 2, 3, 4, 5]
print(f"data = {data_4}")
print("reverse(data)")
print(reverse(data_4))
print("----------------------------------")


def min(data):
    minimum = data[0]
    for number in data:
        if number < minimum:
            minimum = number
    return minimum


data_5 = [5, 4, 2, 8, 1, 6, 3]
print(f"data = {data_5}")
print("min(data)")
print(min(data_5))


def max(data):
    maximum = data[0]
    for number in data:
        if number > maximum:
            maximum = number
    return maximum


print("max(data)")
print(max(data_5))
print("----------------------------------")
