#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
# 1、暴力法 -超时
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            l = r = i
            while l >= 0:
                if heights[l] < heights[i]:
                    break
                l -= 1
            while r < len(heights):
                if heights[r] < heights[i]:
                    break
                r += 1
            res = max(res,heights[i]*(r - l - 1))
        return res
# @lc code=end

