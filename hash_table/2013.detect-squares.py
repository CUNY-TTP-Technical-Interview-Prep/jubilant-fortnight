#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start
from typing import List
from collections import Counter, defaultdict


'''
1. points to keep track of points frequency
2. x_plane keeps track of how many y coordinates exist for any x

add:
  - deconstruct point into x and y
  - points[x, y] += 1
  - x_plane[x].add(y)

count:
  - two possible ways to form a square.
  - positive + negative axis .

  0. break down point into x1 and y1
  3. for each y2 in x_plane[x1]:
    - calculate side length from y2 - y1
    - skip if y1 == y2
    - res += points[x1, y2] * points[x1-side, y2] * points[x1-side, y1]
    - res += points[x, y2] * points[x1+side, y2], points[x1+side, y1]
return res
'''


class DetectSquares:

    def __init__(self):
        self.points = Counter()
        self.x_plane = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.x_plane[x].add(y)

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for y2 in self.x_plane[x1]:
            if y1 != y2:
                side = y2 - y1
                res += self.points[(x1, y2)] * self.points[(x1 +
                                                            side, y2)] * self.points[(x1+side, y1)]
                res += self.points[(x1, y2)] * self.points[(x1 -
                                                            side, y2)] * self.points[(x1-side, y1)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end
