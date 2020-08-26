#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
# 1、reshape排序后二分 31.22%/99.07%
# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix: return target == None
#         mat = []
#         for l in matrix:
#             mat.extend(l)
#         mat.sort()
#         l,r = 0, len(mat) -1
#         while l <= r:
#             mid = (l+r)>>1
#             if mat[mid] == target:
#                 return True
#             elif mat[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return False
# 2、直接暴力法 87.12%/21.16%
# class Solution:
#     def searchMatrix(self, matrix, target):
#         for row in matrix:
#             if target in row:
#                 return True
#         return False
# 3、L形上的元素是有序的 87.12%/92.48%
# 选左下角，往右走增大，往上走减小，可选
# 选右上角，往下走增大，往左走减小，可选
class Solution:
    def searchMatrix(self,  matrix, target):
        if len(matrix) == 0 or len(matrix[0])==0: return target == None
        height,width = len(matrix),len(matrix[0])
        row,col = height - 1,0
        while row >= 0 and col < width:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
        return False


# @lc code=end

