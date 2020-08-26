#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n =  len(p)
        dic = {}
        for i in range(n):
            dic[p[i]] = dic.get(p[i],0)+1
        res = []
        for i in range(len(s)-n):
            k_dic={} #滑动的字典
            for j in range(i,i+n):
                k_dic[s[j]] = k_dic.get(s[j],0) + 1
            if k_dic == dic:
                res.append(i)
            print(k_dic,dic)
        return res

        
# @lc code=end

