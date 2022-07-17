#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
from re import T
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        data structure: dictionary to memoize the valid outputs (may be partially complete)
        set to check for if a word exists in the list

        dfs method => where we recursively check for whether the prefix + suffix of a word are both valid.
        '''
        validWords = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                # check if both prefix and suffix exist in the given list.
                if prefix in validWords and suffix in validWords:
                    memo[word] = True
                    return True
                if prefix in validWords and dfs(suffix):
                    memo[word] = True
                    return True
                if suffix in validWords and dfs(prefix):
                    memo[word] = True
                    return True
            return memo[word]
        res = [word for word in words if dfs(word)]
        return res

# time: O(m * n^3)
# m = nuymber of words
# n = max length of a word within given list.

# @lc code=end


sol = Solution()
words = ["cat", "dog", "catdog"]
words = ["cat", "cats", "catsdogcats", "dog",
                "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]

ans = sol.findAllConcatenatedWordsInADict(words)
print(f'ans: {ans}')
