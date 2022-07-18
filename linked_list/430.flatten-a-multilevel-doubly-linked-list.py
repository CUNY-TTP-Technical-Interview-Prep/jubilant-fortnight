#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node('snail')
        stack = [head]
        prev = dummy
        while stack:
            curr = stack.pop()
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            prev.next = curr
            curr.prev = prev
            curr.child = None
            prev = curr

        node = dummy.next
        node.prev = None
        return node

    def flatten(self, head: 'Optional[Node]'):
        if not head:
            return
        stack = [head]
        flattened = []
        while stack:
            node = stack.pop()
            flattened.append(node)
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)

        for i in range(len(flattened) - 1):
            flattened[i].next = flattened[i+1]
            flattened[i+1].prev = flattened[i]
            flattened[i].child = None
        return flattened[0]


# @lc code=end
