#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if root is None:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        res = dfs(root, 0)  # depth param is missing.
        return res

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        1. [3]
        2. 3 is popped [9, 20] get appended to the queue
        3. 9 is popped. 9 has no left or right children.
          - 20 is popped.

        at each level, pop one single item from the queue
        we check if it has children nodes (left or right)
        if it doesn't, we end the iteration and update the maximum depth value

        if it has a left child, then we push it to the queue
        if it has a right tchild, then we push it to the queue
          - increment depth value individually.
        '''
        if not root:
            return 0
        # queue = [(node, depth_level)]
        # queue = [[3, 1]]
        # queue = [[9, 2], [20, 2]]
        queue = deque([(root, 1)])
        max_depth = 0
        while queue:
            node, depth = queue.popleft()  # pop the leftmost item
            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return max_depth

        # @lc code=end
