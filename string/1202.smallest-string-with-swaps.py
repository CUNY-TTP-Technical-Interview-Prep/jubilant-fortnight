#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    '''
    The core of the idea is that if (0, 1) is an exchange pair and (0, 2) is an exchange pair, then any 2 in (0, 1, 2) can be exchanged.

    This implies, we can build connected components where each component is a list of indices that can be exchanged with any of them. In Union find terms, we simply iterate through each pair, and do a union on the indices in the pair.
    At the end of the union of all the pairs, we have built connected component of indices that can be exchanged with each other.

    Then we build a sorted list of characters for every connected component.

    The final step is, we iterate through all the indices, and for each index we locate its component id and find the sorted list correspondng to that component and grab the next lowest character from that list.

    This way for every index, we find the lowest possible character that can be exchanged and fitted there.
    '''

    def union(self, a, b):
        self.graph[self.find(a)] = self.find(b)

    def find(self, node):
        if self.graph[node] != node:
            self.graph[node] = self.find(self.graph[node])
        return self.graph[node]

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.graph = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)
        group = defaultdict(lambda: ([], []))
        for i, c in enumerate(s):
            root = self.find(i)
            group[root][0].append(i)
            group[root][1].append(c)

        res = [0] * len(s)
        for indices, chars in group.values():
            for i, c in zip(sorted(indices), sorted(chars)):
                res[i] = c
        return ''.join(res)

# @lc code=end


s = "cba"
pairs = [[0, 1], [1, 2]]
s = "dcab"
pairs = [[0, 3], [1, 2]]
s = "dcab"
pairs = [[0, 3], [1, 2], [0, 2]]
sol = Solution()
ans = sol.smallestStringWithSwaps(s, pairs)
print(f'ans: {ans}')
