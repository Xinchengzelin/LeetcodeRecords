#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
# 1、直接递归 19.88%
class Solution:
    import functools
    @functools.lru_cache(None)  #增加这句后99.37%/85.79%
    def fib(self, N: int) -> int:
        return N if N<=1 else self.fib(N-1)+self.fib(N-2)
# 2、记忆化递归：73.89%
# class Solution:
#     def fib(self, N: int) -> int:
#         if N <= 1:
#             return N
#         self.cache={0:0,1:1}
#         return self.memo(N)
#     def memo(self,N):
#         if N in self.cache:
#             return self.cache[N]
#         self.cache[N]= self.memo(N-1)+self.memo(N-2)
#         return self.memo(N)

# 3、动态规划
# class Solution:
#     def fib(self, N: int) -> int:
#         a=[0]*(N+1)
#         a[0]=0
#         a[1]=1
#         for i in range(2,N+1):
#             a[N]=a[N-1]+a[N-2]
#         return a[N]


# @lc code=end

