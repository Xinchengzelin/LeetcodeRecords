#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dic={}
        # for i,v in enumerate(nums):
        #     dic[v]=i
        # for i,v in enumerate(nums):
        #     j=dic.get(target-v)
        #     if j and i != j:
        #         return [i,j]
        
        dic = {}
        for i,num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num],i]
            dic[num] = i
        
# @lc code=end

