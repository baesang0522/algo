"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = len(nums)
        for idx in range(len(nums) - 1):
            if nums[idx + 1] < nums[idx]:
                k = idx + 1
                break
        num1, num2 = nums[:k], nums[k:]

        if num1[0] <= target <= num1[-1]:
            cand_list = num1
            k = 0
        else:
            cand_list = num2

        start, end = 0, len(cand_list)
        while cand_list:
            mid = len(cand_list) // 2
            if cand_list[mid] == target:
                return k + mid
            elif cand_list[mid] > target:
                cand_list = cand_list[start:mid]
            else:
                cand_list = cand_list[mid + 1:end]
                k += mid+1
        return -1
























