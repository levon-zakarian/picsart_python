"""
https://leetcode.com/problems/sum-of-unique-elements/
1748. Sum of Unique Elements
"""

from typing import List


def sumOfUnique(nums: List[int]) -> int:
    sum = 0
    nums_count = {number: nums.count(number) for number in set(nums)}
    for key, value in nums_count.items():
        if value == 1:
            sum += key
    return sum


print(sumOfUnique([1, 2, 3, 2]))
print(sumOfUnique([1, 1, 1, 1, 1]))
print(sumOfUnique([1, 2, 3, 4, 5]))
