#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left != right:

            max_area = max(max_area, (right - left) * 
            min(height[right], height[left]))

            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return max_area



# @lc code=end

