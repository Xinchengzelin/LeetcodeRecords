#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 1、利用队列实现
# class Solution:
#     def levelOrder(self, root: 'Node') -> List[List[int]]:
#         if not root: return []
#         res,queue = [],[root]
#         while queue:
#             level = [] #当前层的结果
#             for _ in range(len(queue)):
#                 node = queue.pop(0)
#                 level.append(node.val)
#                 queue.extend(node.children)
#             res.append(level)
#         return res
# 2、递归 55.06%/31.85%
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root,level):
            if not root:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(root.val)
            for child in root.children:
                dfs(child,level+1)
        res = []
        dfs(root,0)
        return res
# @lc code=end

