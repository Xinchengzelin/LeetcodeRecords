#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 1、递归法  32ms
        if not root:
            return root
        root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
        return root
        #2、迭代-用栈来模拟递归  44ms
        # if not root:
        #     return root
        # stack=[root]
        # while stack:
        #     node=stack.pop()
        #     node.left,node.right=node.right,node.left
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return root
# @lc code=end

