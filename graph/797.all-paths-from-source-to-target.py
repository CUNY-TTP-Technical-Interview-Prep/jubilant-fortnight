#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
from typing import List


class Solution:
    '''
    my approach is using dfs and traverse the neighbors with a current path.

    if we reach the last node, append the path to res
    '''

    def allPathsSourceTarget2(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        # time: o(2^n) => number of edges
        # space: o(n) => number of nodes

        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path)
                return
            for nei in graph[node]:
                dfs(nei, path + [nei])
        dfs(0, [0])
        return res

    def allPathsSourceTarget(self, graph: List[List[int]]):
        res = []
        self.dfs(graph, [0], 0, res)
        return res

    def dfs(self, graph, path, node, res):
        if node == len(graph) - 1:
            res.append(list(path))
            # return not needed because the last node is empty => has no outgoing edges.

        for nei in graph[node]:
            path.append(nei)
            self.dfs(graph, path, nei, res)
            path.pop()


# @lc code=end
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
graph = [[1, 2], [3], [3], []]
sol = Solution()
ans = sol.allPathsSourceTarget(graph)
print(f'ans: {ans}')
