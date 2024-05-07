"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference
between the values of any two different nodes in the tree.

Input: root = [4,2,6,1,3]
Output: 1

Input: root = [1,0,48,null,null,12,49]
Output: 1

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

root = TreeNode(val=4,
                left=TreeNode(val=2,
                              left=TreeNode(val=1, left=None, right=None),
                              right=TreeNode(val=3, left=None, right=None)
                              ),
                right=TreeNode(val=6, left=None, right=None)
                )
"""
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.graph_list = []
        min_gap = 10**5 + 1

        def graph_to_list(root):
            if not root:
                return
            graph_to_list(root.left)
            self.graph_list.append(root.val)
            graph_to_list(root.right)
            return
        graph_to_list(root)
        for idx in range(len(self.graph_list)-1):
            gap = abs(self.graph_list[idx] - self.graph_list[idx + 1])
            if gap <= min_gap:
                min_gap = gap
        return min_gap
