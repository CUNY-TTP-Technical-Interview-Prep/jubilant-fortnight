#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def getKth(self, nums1: List[int], nums2: List[int], low1: int, high1: int, low2: int, high2: int, k: int):
        if low1 > high1:
            # nums1 is exhausted. get the modified kth from nums2 starting here
            return nums2[low2 + k]
        if low2 > high2:
            # nums2 is exhausted. get the modified kth from nums1 starting here
            return nums1[low1 + k]

        mid1 = low1 + (high1-low1)//2
        mid2 = low2 + (high2-low2)//2
        if nums1[mid1] <= nums2[mid2]:
            if k+1 <= (mid1 - low1) + (mid2 - low2) + 1:
                # There are k elements less than number of elements below mid1 + ... mid2 + min(mid1, mid2)
                # mid2 the higher/equal of the comparision can be excluded without removing the kth
                return self.getKth(nums1, nums2, low1, high1, low2, mid2-1, k)
            else:
                # the number of elements below mid1 + ... mid2 + min(mid1, mid2) is lesser than kth position
                # mid1 the lower term can be excluded without removing kth
                return self.getKth(nums1, nums2, mid1 + 1, high1, low2, high2, k - (mid1-low1+1))
                # no. of items below mid1 = mid1-low1
                # and mid1 is 1
        else:  # nums[mid1] > nums[mid2]
            if k+1 <= (mid1 - low1) + (mid2 - low2) + 1:
                # There are k elements less than number of elements below mid1 + ... mid2 + min(mid1, mid2)
                # mid1 the higher of the comparision can be excluded without removing the kth
                return self.getKth(nums1, nums2, low1, mid1-1, low2, high2, k)
            else:
                # the number of elements below mid1 + ... mid2 + min(mid1, mid2) is lesser than kth position
                # mid2 the lower term can be excluded without removing kth
                return self.getKth(nums1, nums2, low1, high1, mid2 + 1, high2, k - (mid2-low2+1))
                # no. of items below mid2 = mid2-low2
                # and mid2 is 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m+n) % 2 == 1:
            return self.getKth(nums1, nums2, low1=0, high1=m-1, low2=0, high2=n-1, k=(m+n)//2)
        else:
            return (self.getKth(nums1, nums2, low1=0, high1=m-1, low2=0, high2=n-1, k=(m+n)//2 - 1) +
                    self.getKth(nums1, nums2, low1=0, high1=m-1, low2=0, high2=n-1, k=(m+n)//2)) / 2.0

# @lc code=end
