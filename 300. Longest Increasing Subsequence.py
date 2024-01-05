"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4

Example 3:
Input: nums = [7, 7, 7, 7, 7, 7, 7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for idx in range(1, n):
            for jdx in range(idx):
                if nums[idx] > nums[jdx]:
                    dp[idx] = max(dp[idx], dp[jdx] + 1)
        return max(dp)
















