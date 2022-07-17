#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
import collections


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        '''
        data structure: dictionary to count the frequency of keys
        max_consecutives
        res

        res < max_consecutives + k
        else:
          we shrink the sliding window by decrrementing the left pointer by 1
        '''

        counter = collections.defaultdict(int)
        max_consecutives = res = 0
        for i in range(len(answerKey)):
            counter[answerKey[i]] += 1
            max_consecutives = max(max_consecutives, counter[answerKey[i]])
            if res < max_consecutives + k:
                res += 1
            else:
                left_pointer = answerKey[i - res]
                counter[left_pointer] -= 1
        return res

        # @lc code=end


answerKey = "TTFF"
k = 2
answerKey = 'TFFK'
k = 1
answerKey = 'TTFTTFTT'
k = 1
answerKey = "FFFTTFTTFT"
k = 3
sol = Solution()
ans = sol.maxConsecutiveAnswers(answerKey, k)
print(f'ans: {ans}')
