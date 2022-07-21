from collections import Counter
from typing import List


class Solution:
    '''
    goal: make the two sums equal

    in one operation: increase or decrease an element to make it another number between 1 => 6.

    approach: use a table to map the possible jumps (either increasing or decreasing) to their respective frequency.
    sum up the arrays and calculate the diff

    starting from 5 (the largest possible jump), iterate thru the table while diff is greater than 0:
      - if table[jump] does not exist: decrement jump by 1 and move onto the next possible jump
      - if jump has reached 0: impossible.
      - else:
          - decrement diff by jump, decrement table[jump], increment the number of steps taken
    '''

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sum(nums2) - sum(nums1)
        if diff < 0:
            return self.minOperations(nums2, nums1)
        count = Counter([6-x for x in nums1] + [x-1 for x in nums2])
        print(f'diff: {diff}')
        print(f'count: {count}')
        jump = 5  # could be either a jump increasing or decreasing
        steps = 0
        while diff > 0:
            if jump == 0:
                return -1
            if count[jump] == 0:
                jump -= 1
            else:
                diff -= jump
                count[jump] -= 1
                steps += 1
        return steps


nums1 = [1, 1]
nums2 = [6]
sol = Solution()
ans = sol.minOperations(nums1, nums2)
print(f'ans: {ans}')
