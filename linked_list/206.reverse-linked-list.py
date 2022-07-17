#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    1. define a dummy node to store the previous node
    2. run a while loop
      - curr => keeps track of the current node
      - nxt = stores the next node before moving the head
      - head => head.next in order to iterate
      - set prev => curr.
    3. return prev.
    '''

    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList(self, head):
        def reverse(node, prev):
            if not node:  # last_node.next
                return prev
            nxt = node.next
            node.next = prev
            return reverse(nxt, node)
        return reverse(head, None)  # null / undefined

# @lc code=end


dummy = ListNode(0)
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
