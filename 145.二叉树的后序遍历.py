#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1、递归法 73.1%/81.51%
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         def postorder(root):
#             if root:
#                 postorder(root.left)
#                 postorder(root.right)
#                 res.append(root.val)
#         res=[]
#         postorder(root)
#         return res
# 2、迭代法 73.1%/81.51%
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:  
        if not root: return []
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.right 
            node = stack.pop()
            cur = node.left
        return res[::-1]
# 2、迭代法2 19.31%/85.97%
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:  
#         if not root: return []
#         res = []
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             res.append(node.val)
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
#         return res[::-1]    

# @lc code=end

