"""
https://leetcode.com/problems/intersection-of-two-arrays/
349. Intersection of Two Arrays
"""

from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))


print(intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
