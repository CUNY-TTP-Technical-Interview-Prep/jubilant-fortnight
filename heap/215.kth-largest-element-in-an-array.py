#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from heapq import heapify, heappop
from typing import List


class Solution:
    '''
    - nums is not sorted.
    - goal: find kth largest element in the sorted array.

    do it without sorting.
    approach: using a min heap to pop out the minimum number n - k times.

    so that the final pop will be our answer.
    '''

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time: O(k + k log n)
        # space: o(n)
        n = len(nums)
        minHeap = nums[:]
        heapify(minHeap)
        for _ in range(n - k):
            heappop(minHeap)
        return heappop(minHeap)


# @lc code=end

nums = [3, 2, 1, 5, 6, 4]
k = 2
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
nums = [2, 1]
k = 1
sol = Solution()
ans = sol.findKthLargest(nums, k)
print(f'ans: {ans}')
