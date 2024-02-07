"""
Given the root of a binary tree and an integer targetSum,
return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result_list, cur_path = [], []
        def dfs(tree_node, cur_path, result_list):
            cur_path.append(tree_node.val)
            if not tree_node.left and not tree_node.right:
                result_list.append(cur_path.copy())
                cur_path.pop()
                return
            if tree_node.left:
                dfs(tree_node.left, cur_path, result_list)
            if tree_node.right:
                dfs(tree_node.right, cur_path, result_list)
            cur_path.pop()
        dfs(root, cur_path, result_list)

        return [path for path in result_list if sum(path) == targetSum]





















