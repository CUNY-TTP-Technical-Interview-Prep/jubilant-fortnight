#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#

# @lc code=start
class Solution:
    '''
    for each jump until we reach n - 1, we want to sum up the possible number of paths
    for each valid numeric key
    '''

    # lichess.org
    # chess.com
    def knightDialer(self, n: int) -> int:
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        for _ in range(n-1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = x6 + x8, x7 + x9, x4 + \
                x8, x3 + x9 + x0, 0, x1 + x7 + x0, x2 + x6, x1 + x3, x2 + x4, x4 + x6
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)

# @lc code=end


sol = Solution()
n = 3131
n = 1
n = 2
ans = sol.knightDialer(n)
print(f'ans: {ans}')
