class Solution:
    def getModfiedArray(self, length, updates):
        res = [0 for _ in range(length)]
        for start, end, x in updates:
            res[start] += x
            if end + 1 < length:
                res[end+1] -= x
        for i in range(1, length):
            res[i] += res[i-1]
        return res


sol = Solution()
length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
length = 10
updates = [[2, 4, 6], [5, 6, 8], [1, 9, -4]]
ans = sol.getModfiedArray(length, updates)
print(f'ans: {ans}')
