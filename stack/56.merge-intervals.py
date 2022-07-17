#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        1. sort the intervals by the beginning.
        2. stack = keep track of the overlapping intervals.
        3. iterate over the intervals
          - if stack is not empty and if the ending of the last item in my stack is less than the ending of the current interval.
        '''
        stack = []
        # curr = current interval
        for curr in sorted(intervals, key=lambda interval: interval[0]):
            if stack and curr[0] <= stack[-1][-1]:
                # before we compare, check if beginning of the current interval is
                # less than or equal to the end of the previous interval
                # compare the two endings: prev interval vs current interval.
                # let the stack be modified by the greater one.
                # ex: [[1,6], [7,10]] => not valid to be overlapped.
                # ex: [[1,5], [3, 8]] => [[1,8]]
                # 1st iteration: [1,5]
                # 2nd iteration: compare 5 vs 8 => [1,5] => becomes [1,8]
                stack[-1][-1] = max(stack[-1][-1], curr[-1])
            else:
                stack.append(curr)
        return stack

# @lc code=end
