#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
from re import L
from typing import List


class Solution:
    '''
    an array with an arbitray length of 3 will fit the purpose.
    for loop
      - compare the current num with each values in our dummy array.
      - update the array accordingly by moving it up one index at a time, while carrying along the previous elements.
    '''

    def thirdMax(self, nums: List[int]) -> int:
        dummy = [float('-inf') for _ in range(3)]  # length of 3
        for n in nums:
            if n not in dummy:
                if n > dummy[0]:
                    dummy = [n, dummy[0], dummy[1]]
                elif n > dummy[1]:
                    dummy = [dummy[0], n, dummy[1]]
                elif n > dummy[2]:
                    dummy = [dummy[0], dummy[1], n]
        return dummy[2] if float('-inf') not in dummy else max(dummy)

# @lc code=end


sol = Solution()
nums = [3, 2, 1]
ans = sol.thirdMax(nums)
print(f'ans: {ans}')
