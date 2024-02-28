"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.


Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        left_val = None

        while queue:
            node = queue.popleft()
            left_val = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return left_val


tn = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(
            val=4,
            left=None,
            right=None,
        ),
        right=None
    ),
    right=TreeNode(
        val=3,
        left=TreeNode(
            val=5,
            left=TreeNode(
                val=7,
                left=None,
                right=None
            ),
            right=None
        ),
        right=TreeNode(
            val=6,
            left=None,
            right=None
        )
    )
)


s = Solution()
aa = s.diameterOfBinaryTree(tn)






