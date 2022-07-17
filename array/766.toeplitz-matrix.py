#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # nested for loop to compare the elements along the diagonal line
        for i in range(len(matrix)-1):
            for j in range(len(matrix[i])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

# @lc code=end


matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
matrix = [[1, 2], [2, 2]]

sol = Solution()
ans = sol.isToeplitzMatrix(matrix)

print(f'ans: {ans}')
