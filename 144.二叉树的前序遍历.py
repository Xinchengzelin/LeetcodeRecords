#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归法 44 ms
        # def preorder(root):
        #     if root:
        #         res.append(root.val)
        #         preorder(root.left)
        #         preorder(root.right)
        # res=[]
        # preorder(root)
        # return res

        # 迭代法 44 ms
        if not root: return []
        res=[]# 如果res=stack =[]是错误的，list是可变的，这样res和stack指向同一个变量
        stack=[]
        cur=root
        while stack or cur:
            while cur:#所有父节点进结果，将左节点压入栈
                res.append(cur.val)
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            cur=cur.right
        return res
        # 迭代法-注意入栈先是右节点，后左节点
        # if not root:
        #     return []    
        # res = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return res

        

# @lc code=end

