#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict, deque
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times, N, K):
        # time: O(E)
        # space: O(E+V)
        queue = deque([K])
        weights = defaultdict(dict)
        for u, v, time in times:
            weights[u][v] = time
        dist = [float('inf') for _ in range(N+1)]
        dist[0] = 0
        dist[K] = 0
        while queue:
            u = queue.popleft()
            for v in weights[u]:
                t = dist[u] + weights[u][v]
                if t < dist[v]:
                    dist[v] = t
                    queue.append(v)
        return max(dist) if max(dist) < float('inf') else -1

    def networkDelayTimeHeap(self, times, N, K):  # O(E + VlogV); o(V+e)
        weights = defaultdict(dict)
        for u, v, t in times:
            weights[u][v] = t
        minHeap = [(0, K)]  # (time, source node)
        dist = {}
        while minHeap:
            time, u = heappop(minHeap)
            if u not in dist:
                dist[u] = time
                for v in weights[u]:
                    heappush(minHeap, (time + weights[u][v], v))
        return max(dist.values()) if len(dist) == N else -1

# @lc code=end


times = [[1, 2, 1]]
n = 2
k = 2

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
sol = Solution()
ans = sol.networkDelayTime(times, n, k)
print(f'ans: {ans}')
