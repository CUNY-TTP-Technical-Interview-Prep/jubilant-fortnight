#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
from collections import defaultdict
from random import choice


class RandomizedSet:

    def __init__(self):
        self.val_indices = defaultdict(int)
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.val_indices:
            return False
        self.val_indices[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_indices:
            return False
        i = self.val_indices[val]
        last = self.list[-1]
        # swap items before popping the last.
        self.list[i], self.list[-1] = last, val
        self.val_indices[last] = i
        self.val_indices.pop(val)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.list)

# @lc code=end
