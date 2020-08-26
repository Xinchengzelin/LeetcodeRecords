#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_min=nums.copy()
        for i in range(len(nums)):
            dp_min[i]=min(dp_min[i-1]*nums[i],nums[i],nums[i-1]*nums[i])
            nums[i]=max(nums[i-1]*nums[i],nums[i],dp_min[i-1]*nums[i])
        print(dp_min,nums)
        return max(nums)
# @lc code=end

