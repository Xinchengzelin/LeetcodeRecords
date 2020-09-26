#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left,right):
            if left > right:
                return None
            val = postorder.pop()#关键
            index = dic[val]
            root = TreeNode(val)
            root.right = helper(index+1,right)#右子树在前，
            #如果按每次选择「后序遍历的最后一个节点」为根节点，则先
            # 被构造出来的应该为右子树。
            root.left = helper(left,index-1)
            return root
        dic = {v:k for k,v in enumerate(inorder)}
        return helper(0,len(inorder)-1)
# @lc code=end

