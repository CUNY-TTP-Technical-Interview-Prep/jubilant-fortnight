# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_idx, max_idx = 0, 0
        table = {}
        queue = deque([(root, 0)])
        while queue:
            node, idx = queue.popleft()
            if idx not in table:
                table[idx] = [node.val]
            else:
                table[idx].append(node.val)
            i, j = idx - 1, idx + 1
            if node.left:
                min_idx = min(min_idx, i)
                queue.append((node.left, i))
            if node.right:
                max_idx = max(max_idx, j)
                queue.append((node.right, j))

        return [table[i] for i in range(min_idx, max_idx)]
