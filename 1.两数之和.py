#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        index = 0
        for item in nums:

            if target - item in dict:
                return [index, dict[target-item]]

            dict[item] = index
            index += 1

# @lc code=end

