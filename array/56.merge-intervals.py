#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    '''
    my approach:
    first sort the intervals by the start.
    data structure: a stack.
    iterate over the sorted intervals, compare the ending of last item in the stack against the current start.

    comparison: >=

    if true, let new ending be the max of (last ending, new ending)
    '''

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(n log n)
        # space: O(n)
        stack = []
        for start, end in sorted(intervals, key=lambda i: i[0]):
            if stack and stack[-1][-1] >= start:
                stack[-1][-1] = max(stack[-1][-1], end)
            else:
                stack.append([start, end])
        return stack

# @lc code=end


intervals = [[1, 4], [0, 4]]
intervals = [[1, 4], [2, 3]]
intervals = [[1, 4], [4, 5]]
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
sol = Solution()
ans = sol.merge(intervals)
print(f'ans: {ans}')
