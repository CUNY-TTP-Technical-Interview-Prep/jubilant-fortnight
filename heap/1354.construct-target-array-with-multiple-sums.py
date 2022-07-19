#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#

# @lc code=start

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    '''
    algorithm:
    - total sum is always bigger than each single one of all elements.
    - at each iteration, we can pull out the largest number, then subtract the sum of other elements from this current maximum number.

    base case:
    if we reach n == 1 or total  == 1:
      return True
    else if n < current total or total == 0 or n % total == 0:
      return False

    before moving on to the next iteration, update the current total by adding the updated n.
    '''

    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        minHeap = [-n for n in target]
        heapify(minHeap)
        while True:
            currMax = -heappop(minHeap)
            total -= currMax
            if currMax == 1 or total == 1:
                return True
            if currMax < total or total == 0 or currMax % total == 0:
                return False
            currMax %= total
            total += currMax
            heappush(minHeap, -currMax)

# @lc code=end


target = [1, 1, 1, 2]
target = [8, 5]
target = [9, 3, 5]
sol = Solution()
ans = sol.isPossible(target)
print(f'ans: {ans}')
