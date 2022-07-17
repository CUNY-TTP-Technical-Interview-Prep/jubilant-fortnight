from collections import defaultdict


class Solution:
    def lengthOfLongestSubstr(self, s, k):
        d = defaultdict(int)
        i, res = 0, 0
        for j in range(len(s)):
            d[s[j]] += 1
            if len(d) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
            res = max(res, j - i + 1)
        return res


sol = Solution()
s, k = 'eceba', 2
s, k = 'aa', 1
ans = sol.lengthOfLongestSubstr(s, k)
print(f'ans: {ans}')
