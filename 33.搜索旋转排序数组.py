#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
# 1、二分查找  49.25%
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return -1
#         l,r=0,len(nums)-1
#         #[l, mid] 和 [mid + 1, r]至少一个有序
#         while l <= r:
#             mid=(l+r)//2
#             if target == nums[mid]:
#                 return mid
#             if nums[0]<=nums[mid]:#[0,mid]是排序的
#                 if nums[0] <= target <= nums[mid]:
#                     r=mid-1
#                 else:
#                     l=mid+1
#             else:#if nums[0]>nums[mid]:#[0,mid]存在旋转位,即nums[0]>nums[mid]
#                 #target<nums[mid] 或 target>nums[0]向前规约
#                 if target >= nums[0] or target < nums[mid]:
#                     r=mid-1
#                 else:
#                     l=mid+1
#         return -1

# 2、二分法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]: # [0,mid]有序
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: #  [mid,len(nums)-1]有序
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1
# @lc code=end

