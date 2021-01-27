#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i-1] == nums[i]:
                continue

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    tmp = nums[right]

                    while (left < right and tmp == nums[right]):
                        right -= 1

                    tmp = nums[left]
                    while (left < right and tmp == nums[left]):
                        left += 1

                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        
        return res




# @lc code=end

