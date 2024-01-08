"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List


def two_pointer(target_list, target):
    low, high = 0, len(target_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if target_list[mid] == target:
            return "Find"
        elif target_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low if low == 0 else low - 1


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        fst_m = [row[0] for row in matrix]

        matrix_idx = two_pointer(target_list=fst_m, target=target)
        if matrix_idx == "Find":
            return True
        else:
            result = two_pointer(target_list=matrix[matrix_idx], target=target)
            if result == "Find":
                return True
            else:
                return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
# matrix = [[1]]
# target = 1


s = Solution()
ss = s.searchMatrix(matrix=matrix, target=target)


#
# fst_m = [row[0] for row in matrix]
# def two_pointer(target_list, target):
#     low, high = 0, len(target_list) - 1
#     mid = (low + high) // 2
#
#     while low < high:
#         if target_list[mid] == target:
#             return "Find"
#         elif target_list[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low
#
# def binary_search(target_list, target):
#     mid = tar
#
#
#
# ss = two_pointer(matrix, target)














