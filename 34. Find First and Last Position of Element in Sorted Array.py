"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        idx = bisect.bisect_left(nums, target)
        if idx < len(nums) and target == nums[idx]:
            ans.append(idx)
        else:
            return [-1, -1]

        idx = bisect.bisect_right(nums, target)
        if idx > 0 and nums[idx - 1] == target:
            ans.append(idx - 1)
        return ans


# class Solution:
#     def searchRange(self, nums, target):
#         start, end = 0, len(nums)-1
#
#         left, right = self.searchLeft(nums, target), self.searchRight(nums, target)
#         result = [left, right]
#         return result
#
#     def searchLeft(self, nums, target):
#         start, end = 0, len(nums)-1
#         result = -1
#         while start <= end:
#             mid = int((start+end)/2)
#             if nums[mid] == target:
#                 result = mid
#                 end = mid - 1
#             elif nums[mid] < target:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         return result
#
#     def searchRight(self, nums, target):
#         start, end = 0, len(nums)-1
#         result = -1
#         while start <= end:
#             mid = int((start+end)/2)
#             if nums[mid] == target:
#                 result = mid
#                 end = mid + 1
#             elif nums[mid] < target:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         return result
































