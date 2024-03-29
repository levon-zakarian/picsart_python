"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def fibonacci(n):
    first = 1
    seconds = 2

    while n > 1:
        first, seconds = seconds, first + seconds
        n -= 1
    return first


num = 1
fib_num = 0
sum = 0
while fib_num < 4000000:
    fib_num = fibonacci(num)
    if num % 2 == 0:
        sum += fib_num
    num += 1

print(sum)
