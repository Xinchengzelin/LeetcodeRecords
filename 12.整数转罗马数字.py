#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
# 方法1
        # res = []
        # dic ={1:"I", 4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        # l = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        # i = 0
        # while num > 0:
        #     while num >= l[i]:
        #         res.append(dic[l[i]])
        #         num = num - l[i]
        #     i += 1
        # return "".join(res)
# 方法2
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res, i = "", 0
        while num:
            res += (num//values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res
# @lc code=end

