from curses.ascii import isspace


class Solution:
    def trim_trailing_spaces(self, t):
        if ''.join(t).isspace():
            return []
        l, r = 0, len(t)-1
        while l < r and t[l].isspace():
            l += 1
        while l < r and t[r].isspace():
            r -= 1
        return t[l:r+1]

    def reverse_string(self, t, l, r):
        while l < r:
            t[l], t[r] = t[r], t[l]
            l += 1
            r -= 1

    def reverse_sentence(self, t):
        l = r = 0
        while r < len(t):
            while r < len(t) and not t[r].isspace():
                r += 1
            self.reverse_string(t, l, r-1)
            r += 1
            l = r

    def trim_spaces(self, s):
        res = []
        for i in range(len(s)):
            if res and res[-1].isspace() and s[i].isspace():
                continue
            res.append(s[i])
        return res

    def reverseWords(self, s: str) -> str:
        t = list(s)
        t = self.trim_trailing_spaces(t)
        self.reverse_string(t, 0, len(t)-1)
        self.reverse_sentence(t)
        t = self.trim_spaces(t)
        return ''.join(t)


sol = Solution()
s = "the sky is blue"
s = "a good   example"
s = "  hello world  "
ans = sol.reverseWords(s)
print(f'ans: {ans}')
