#
# @lc app=leetcode id=1553 lang=python3
#
# [1553] Minimum Number of Days to Eat N Oranges
#

# @lc code=start


from collections import defaultdict


class Solution:
    def minDays(self, n: int) -> int:
        cache = defaultdict(int)
        cache[0] = 0
        cache[1] = 1

        def dfs(n):
            if n in cache:
                return cache[n]
            print(f'{n} % 2: {n % 2}')
            print(f'{n} % 3: {n % 3}')
            days = 1 + min(n % 2 + dfs(n - n//2), n %
                           3 + dfs(n - (2 * (n // 3))))
            cache[n] = days
            return cache[n]
        return dfs(n)

# @lc code=end


n = 6
n = 10
sol = Solution()
ans = sol.minDays(n)
print(f'ans: {ans}')
