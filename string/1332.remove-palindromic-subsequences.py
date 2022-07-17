#
# @lc app=leetcode id=1332 lang=python3
#
# [1332] Remove Palindromic Subsequences
#

# @lc code=start
class Solution:
    '''
    subsequence = a string taken from another string by deleting some characters while maintaining the order.

    ex:
    s = "ababa"
    subseq = 'aaa' or 'abb' or 'abaa' or 'bba'

    scenarios:
    1. s is a palindrome, so it takes 1 step to remove it.
    2. s is empty, it takes 0 step to remove it.
    3. s is not a palindrome, we can take 2 stesp to do
      - remove all the 'a's
      - remove all the 'b's
      - all that is left is an empty string
    '''

    def removePalindromeSub(self, s: str) -> int:
        def isPalindrome(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return isPalindrome(i+1, j-1)
        pali = isPalindrome(0, len(s)-1)
        return 2 - pali - (s == "")


# @lc code=end
sol = Solution()
s = "abb"
s = "baabb"
s = "ababa"

ans = sol.removePalindromeSub(s)
print(f'ans: {ans}')
