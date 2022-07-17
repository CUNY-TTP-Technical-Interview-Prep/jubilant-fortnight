#
# @lc app=leetcode id=1583 lang=python3
#
# [1583] Count Unhappy Friends
#
from collections import defaultdict
from typing import List
# @lc code=start


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairsMap = defaultdict(int)  # keep track of whom is paried with whom
        # keeps track of each person's preference scores in relation to the others.
        preferenceScores = {}
        for x, y in pairs:
            pairsMap[x] = y
            pairsMap[y] = x

        for i in range(n):
            for j in range(n-1):
                # j = the actual preference score
                # person of interest = preferences[i][j]
                if i not in preferenceScores:
                    preferenceScores[i] = {}
                preferenceScores[i][preferences[i][j]] = j

        res = 0
        for i in range(n):
            for j in range(n-1):
                # the lower the j value, the higher the preference.
                x = i
                y = pairsMap[x]
                u = preferences[i][j]
                v = pairsMap[u]
                if preferenceScores[x][u] < preferenceScores[x][y] and preferenceScores[u][x] < preferenceScores[u][v]:
                    res += 1
                    break

        return res


# @lc code=end
sol = Solution()

n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]

n = 2
preferences = [[1], [0]]
pairs = [[1, 0]]

n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]

ans = sol.unhappyFriends(n, preferences, pairs)
print(f'ans: {ans}')
