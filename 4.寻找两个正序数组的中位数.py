#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        i = 0
        j = 0
        tmp = 0

        for ix in range((m+n)//2 + 1):
            tmp2 = tmp

            if (i < n and (j >= m or nums1[i] < nums2[j])):
                tmp = nums1[i]
                i += 1
            else:
                tmp = nums2[j]
                j += 1

        if (m+n) & 1 == 0:
            return (tmp + tmp2)/2 
        else:
            return tmp
        


            

# @lc code=end

