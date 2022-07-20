#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
from typing import List


class Solution:
    '''
    dfs approach
    - a path documenting my potential valid sentence
    - an index telling me where to start attacking the string.
    - at each iteration, come up with a substring and see if it exists in the dictionary.
    - if we successfully reach the last index, then we have found a valid sentence => add it to the final result.

    In the worst case the runtime of this algorithm is O(2^n).

    Consider the input "aaaaaa", with wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaa"]. Every possible partition is a valid sentence, and there are 2^n-1 such partitions. It should be clear that the algorithm cannot do better than this since it generates all valid sentences. The cost of iterating over cached results will be exponential, as every possible partition will be cached, resulting in the same runtime as regular backtracking. Likewise, the space complexity will also be O(2^n) for the same reason - every partition is stored in memory.
    '''

    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordSet = set(wordDict)

        def dfs(i, path):
            if i == len(s):
                res.append(' '.join(path))
            for j in range(i, len(s)):
                subs = s[i:j+1]
                if subs in wordSet:
                    path.append(subs)
                    dfs(j+1, path)
                    path.pop()
        dfs(0, [])
        return res

    def wordBreak(self, s: str, wordDict):
        memo = {}
        res = []

        def dfs(i):
            t = s[i:]
            if not t:
                return []
            if t in memo:
                return memo[t]

            path = []
            for word in wordDict:
                if t.startswith(word):
                    if t == word:
                        path.append(word)
                    else:
                        t2 = t[len(word):]
                        subpath = dfs(i+len(word))
                        for subs in subpath:
                            path.append(word + ' ' + subs)
            memo[t] = path
            return path

        return dfs(0)

# @lc code=end


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
sol = Solution()
ans = sol.wordBreak(s, wordDict)
print(f'ans: {ans}')
