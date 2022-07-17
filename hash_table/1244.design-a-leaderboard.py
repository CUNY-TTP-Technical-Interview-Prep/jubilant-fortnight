from heapq import heappush, heappop
from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)
        self.minHeap = []

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        res = 0
        for v in self.board.values():
            heappush(self.minHeap, v)
            while len(self.minHeap) > K:
                heappop(self.minHeap)
        while self.minHeap:
            res += self.minHeap.pop()
        return res

    def reset(self, playerId: int) -> None:
        del self.board[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
