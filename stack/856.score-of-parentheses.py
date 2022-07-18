#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    '''
    parent nodes => leaf nodes
    each level we go down, we multiply the sum by two.

    depth = 0
    for each () encountered, we increment `res` by 2**(level of depth)
    '''

    def scoreOfParentheses(self, s: str) -> int:
        res = depth = 0
        for a, b in zip(s, s[1:]):
            if a + b == '()':
                res += 2 ** depth
            depth += 1 if a == '(' else -1
        return res

# @lc code=end


s = '()'
s = '(()(()()))'
s = '((()))'
sol = Solution()
ans = sol.scoreOfParentheses(s)
print(f'ans: {ans}')
