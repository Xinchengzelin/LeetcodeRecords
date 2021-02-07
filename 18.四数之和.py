#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        1、关键点：l，r先改变，j其次，i最后
        2、提前剪枝，可以优化时间
        '''
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l,r = j+1,len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] +nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r-1 and nums[l+1] == nums[l]:
                            l += 1
                        while l < r-1 and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    elif s > target:
                        r -= 1
        return res

# @lc code=end

