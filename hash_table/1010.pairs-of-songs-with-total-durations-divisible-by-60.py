#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start

from re import L
from typing import List


class Solution:
    '''
    goal; find a pair of songs where
    (time[i] + time[j]) % 60 == 0.

    approach: two-sum
    hash table mapping each minute to its frequency count.
    '''

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        count = [0] * 60
        for t in time:
            t2 = -t % 60
            res += count[t2]
            # storing the remainder of the previous time. so that next time we encounter it, we know it's a valid pair.
            count[t % 60] += 1
        return res


# @lc code=end


time = [30, 20, 150, 100, 40]
time = [60, 60, 60]
sol = Solution()
ans = sol.numPairsDivisibleBy60(time)
print(f'ans: {ans}')
