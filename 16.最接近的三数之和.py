#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        res = float('INF')
        for i in range(len(nums)):
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right] 
                if s == target:
                    return s
                elif s > target:
                    right -= 1

                    if abs(res - target) > abs(s - target):
                        res = s

                else:
                    left += 1

                    if abs(res - target) > abs(s - target):
                        res = s
                    

        return res



# @lc code=end

