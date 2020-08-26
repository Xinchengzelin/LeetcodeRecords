#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1、BFS  88.17%
# class Solution:
#     def largestValues(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         stack,res=[root],[]
#         while stack:
#             level=[]
#             next_level=[]#while下一次循环的stack
#             for item in stack:
#                 level.append(item.val)
#                 if item.left:
#                     next_level.append(item.left)
#                 if item.right:
#                     next_level.append(item.right)
#             stack=next_level
#             res.append(max(level))
#         return res

# 2、BFS-列表推导式 72.67%
# class Solution:
#     def largestValues(self, root: TreeNode) -> List[int]:
#         # if not root: return []
#         stack,res=[root],[]
#         while root and stack:#有root就不需要前面的if not root了
#             res.append(max([v.val for v in stack]))
#             stack=[kid for node in stack for kid in (node.left,node.right) if kid]
#         return res

# 3、DFS  72.67%
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res=[]
        def dfs(root,level):
            if not root:
                return
            if len(res)==level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                dfs(root.left,level+1)
            if root.right:
                dfs(root.right,level+1)
        dfs(root,0)
        return [max(l) for l in res]
            
        
# @lc code=end

