# class Solution:
#     def search(self, nums):
#         l,r=0,len(nums)-1
#         while l < r:
#             mid = (l+r)//2
#             if nums[l] <= nums[mid]:
#                 l = mid
#             elif nums[l] > num[mid]:
#                 r = mid


# Solution().search([4, 5, 6, 7, 0, 1, 2])
# class Solution:
#     memo=[]
#     def fib(self,n):
#         if n<=1: return n
#         if memo[n]==0:
#             memo[n]=self.fib(n-1)+self.fib(n-2)
#         print(memo)
#         return memo[n]
# print(Solution().fib(6))
# print(Solution().fib(3))
# print(Solution().fib(30))


# print([[1]*3] )

# c = 2.0
# d = 2.0
# e = d
# print(id(c),id(d),id(e),id(2.0))
# print('c == d:',c==d)
# print('c is d:',c is d)

# e=3.0
# c=4.0
# print("**",id(c),id(d),id(e),id(2.0),id(3.0))

# print(" ".rstrip(" ").split(" ")[-1])
# print(list(" ".rstrip(" ")))
# print(list(" ".rstrip()))
# print(" ".rstrip().split(" ")[-1])

print(0 or -1)