#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
from typing import List


class Solution:
    '''
    1. send all people to city A
    2. then calculate the difference between
    the two cities. b - a for a, b in costs
    3. swap out people from city A to city B where it makes the most economic sense (where the diff from step 2 is bigger than the rest.)
    4. apply step 3 only only to half number of people.
    '''

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        first_city = sum(a for a, b in costs)
        differences = [b - a for a, b in costs]
        differences.sort()
        return first_city + sum(differences[:n // 2])

# @lc code=end


costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
costs = [[515, 563], [451, 713], [537, 709], [343, 819],
         [855, 779], [457, 60], [650, 359], [631, 42]]
sol = Solution()
ans = sol.twoCitySchedCost(costs)
print(f'ans: {ans}')
