"""
https://leetcode.com/problems/degree-of-an-array/
697. Degree of an Array
"""

from typing import List
from collections import Counter


def findShortestSubArray(nums: List[int]) -> int:
    # Count the occurrences of each number keep in a dict
    nums_count = dict((number, nums.count(number)) for number in set(nums))
    # Get most repeated number key
    most_nums = max(nums_count, key=nums_count.get)
    # Filter the dict with only maximum count numbers
    nums_count = {
        key: value
        for key, value in nums_count.items()
        if value == nums_count[most_nums]
    }
    # Find the lengths of sublists
    sublist_lengths = []
    for num in nums_count:
        start = nums.index(num)
        end = len(nums) - nums[::-1].index(num)
        sublist_lengths.append(len(nums[start:end]))

    return min(sublist_lengths)


print(findShortestSubArray([1, 2, 2, 3, 1]))
print(findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
print(findShortestSubArray([1, 5, 2, 3, 5, 4, 5, 6]))
