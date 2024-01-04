# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def recursion(node):
            if node is None:
                return
            recursion(node.left)
            nodes.append(node)
            recursion(node.right)

        recursion(root)
        sorted_nodes = sorted(nodes, key=lambda x: x.val)
        for idx in range(len(sorted_nodes)):
            if sorted_nodes[idx].val != nodes[idx].val:
                sorted_nodes[idx].val, nodes[idx].val = nodes[idx].val, sorted_nodes[idx].val
                break

        result = []
        need_visit = [root]
        while need_visit:
            node = need_visit.pop(0)
            result.append(node.val)
            if node.left:
                need_visit.append(node.left)
            if node.right:
                need_visit.append(node.right)
        return result
