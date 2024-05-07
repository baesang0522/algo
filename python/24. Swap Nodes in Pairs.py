"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes(i.e., only nodes themselves may be changed.)


Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        checker = 0
        def recursion_swap(head, checker):
            if not head:
                return
            if checker % 2 == 0:
                recursion_swap(head.next, checker=checker+1)
                if not head.next:
                    return
                head.val, head.next.val = head.next.val, head.val
            else:
                recursion_swap(head.next, checker=checker+1)
        recursion_swap(head, checker=checker)
        return head
#
#
# ln = ListNode(
#     val=1,
#     next=ListNode(
#         val=2,
#         next=ListNode(
#             val=3,
#             next=ListNode(
#                 val=4,
#                 next=None
#             )
#         )
#     )
# )
# # ln = ListNode(
# #     val=1,
# #     next=None
# # )
#
# s = Solution()
# aa = s.swapPairs(ln)
#
# val_list = []
# def collect_val(list_node, val_list):
#     if not list_node:
#         return
#     val_list.append(list_node.val)
#     collect_val(list_node.next, val_list)
# collect_val(aa, val_list)
#


















