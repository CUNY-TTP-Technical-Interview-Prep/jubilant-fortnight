#
# @lc app=leetcode id=1471 lang=python3
#
# [1471] The k Strongest Values in an Array
#

# @lc code=start
from typing import List


# time: o(nlogn)
class Solution:
    '''
    a num is stronger if:
    arr[j] if |arr[i] - m| > |arr[j] - m|

    if |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j] if arr[i] > arr[j].
    '''

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        # two pointers i and j
        n = len(arr)
        i, j = 0, n - 1
        m = arr[(n - 1) // 2]
        while n + i - j - 1 < k:
            if m - arr[i] > arr[j] - m:
                i += 1
            else:
                j -= 1
        return arr[:i] + arr[j+1:]

# @lc code=end


sol = Solution()
arr = [1, 1, 3, 5, 5]
k = 2
arr = [1, 2, 3, 4, 5]
k = 2
ans = sol.getStrongest(arr, k)
print(f'ans: {ans}')
