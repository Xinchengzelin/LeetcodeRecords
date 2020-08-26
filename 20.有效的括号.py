#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # #1、栈解法
        # dic={")":"(","]":"[","}":"{"}
        # stack=[]
        # for c in s:
        #     if c in dic.values():
        #         stack.append(c)
        #     elif c in dic.keys():
        #         if stack==[] or stack.pop()!=dic[c]:#or前后条件顺序不能换，可能会有[].pop()而报错
        #             return False
        #     else:
        #         return False
        # return stack==[]
        # 2、栈-优化代码
        dic={")":"(","]":"[","}":"{"}
        stack=[]
        for c in s:
            if c in dic.keys():
                top_ele=stack.pop() if stack else "@"
                if top_ele != dic[c]:
                    return False
            else:
                stack.append(c)
        return stack==[]
# @lc code=end

