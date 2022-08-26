"""
https://leetcode.com/problems/build-an-array-with-stack-operations/
1441. Build an Array With Stack Operations
"""

from typing import List


def buildArray(target: List[int], n: int) -> List[str]:
    stack = []
    operations = []
    location = 0
    for i in range(n):
        if stack != target:
            stack.append(i + 1)
            operations.append("Push")
            if stack[location] < target[location]:
                stack.pop()
                operations.append("Pop")
                continue
            location += 1
            continue
    return operations


print(buildArray(target=[1, 3], n=3))
print(buildArray(target=[1, 2, 3], n=3))
print(buildArray(target=[1, 2], n=4))
print(buildArray(target=[2, 3, 4], n=4))
