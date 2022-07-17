#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
import math
from typing import List


class Solution:
    '''
    reqs:
    - width must not exceed length
    - diff between width && length must be minimum

    appraoch: get square root of the target area => which will return a number closesst to the center
    from there we can run a while loop to exhaust the width by decremneting by 1 at each iteration. until area is fully divisible by width.
    '''

    def constructRectangle(self, area: int) -> List[int]:
        width = int(math.sqrt(area))
        while area % width:
            width -= 1
        return [area // width, width]

# @lc code=end


area = 37
area = 122122
sol = Solution()
ans = sol.constructRectangle(area)
print(f'ans: {ans}')
