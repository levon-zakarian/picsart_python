"""
https://leetcode.com/problems/sort-array-by-parity/
905. Sort Array By Parity
"""

from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    sorted_array, odds_array = [], []
    for number in nums:
        if number % 2 == 0:
            sorted_array.append(number)
        else:
            odds_array.append(number)
    sorted_array.extend(odds_array)
    return sorted_array


print(sortArrayByParity([3, 1, 2, 4]))
print(sortArrayByParity([0]))
print(sortArrayByParity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
