#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
        # 迭代法 76.55%/79.16%
        # prev=None
        # cur=head
        # while cur:
        #     temp=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=temp
        # return prev

        #递归法 91.15%/6.82%
        # if not head or not head.next:
        #     return head
        # # drill down
        # newNode=self.reverseList(head.next)
        # head.next.next=head
        # head.next=None
        # return newNode
        # 递归的意思：我子节点下的所有节点都已经反转好了，现在就剩我和我的子节点 
        # 没有完成最后的反转了，所以反转一下我和我的子节点。
        # 不妨假设链表为1，2，3，4，5。按照递归，当执行reverseList（5）的时候返回
        # 了5这个节点，reverseList(4)中的p就是5这个节点，我们看看reverseList（4）
        # 接下来执行完之后，5->next = 4, 4->next = null。这时候返回了p这个节点，也
        # 就是链表5->4->null，接下来执行reverseList（3），解析为4->next = 3,
        # 3->next = null，这个时候p就变成了，5->4->3->null, reverseList(2),
        #  reverseList(1)依次类推，p就是:5->4->3->2->1->null
# 3、好理解的递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(nod,prev):
            if not nod:
                return prev
            # 处理当前层
            next_node = nod.next
            nod.next = prev
            #drill down
            return reverse(next_node,nod)#注意这个return
        return reverse(head,None) #注意这个return

# @lc code=end

