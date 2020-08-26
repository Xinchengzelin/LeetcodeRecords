# # 1、冒泡排序-代码最简单,将最大的元素依次放到后面（也可以将最小的元素放到最前面）
# class Solution:
#     def Sort(self,arr):
#         n = len(arr)
#         for i in range(n-1):
#             for j in range(0,n-i-1):
#                 if arr[j] > arr[j+1]:
#                     arr[j+1],arr[j] = arr[j],arr[j+1]
#         print(arr)
# # 2、选择排序-找到最小值，放在最前面
# class Solution:
#     def Sort(self,arr):
#         for i in range(len(arr)):
#             minIndex = i
#             for j in range(i,len(arr)):
#                 if arr[minIndex] > arr[j]:
#                     minIndex = j
#             arr[minIndex],arr[i] = arr[i],arr[minIndex]
#         print(arr)
# # 3、插入排序-将剩余元素逐步插入前面的排序数组中
# class Solution:
#     def Sort(self,arr):
#         for i in range(1,len(arr)):
#             key = arr[i]#key是拿出排序的元素
#             j = i - 1
#             while j >= 0 and arr[j] > key:
#                 arr[j+1] = arr[j]
#                 j -= 1
#             arr[j+1] = key#注意是j+1 
#         print(arr)
# # 4、快速排序 - 分治，直接修改数组in place
# class Solution:            
#     def Sort(self,begin,end,arr):
#         if begin >= end:
#             return
#         pivot_index = self.partion(begin,end,arr)
#         self.Sort(begin,pivot_index-1,arr)
#         self.Sort(pivot_index+1,end,arr)
#         print(arr)

#     def partion(self,begin,end,num):
#         pivot=end #标杆位置
#         counter = begin #小于标杆的个数
#         for i in range(begin,end):
#             if num[i] < num[pivot]:
#                 num[i],num[counter] = num[counter],num[i]
#                 counter += 1
#         num[pivot],num[counter] = num[counter],num[pivot]#pivot_index前面都小于，后面都大于等于
#         return counter
# # 5、归并排序 - 分成两个长度n/2的序列，然后分别排序（递归排序），最后合并
class Solution:            
    def Sort(self,left,right,arr):
        if left >= right:
            return
        mid = (left + right) >> 1
        self.Sort(left,mid,arr)
        self.Sort(mid+1,right,arr)
        self.merge(left,right,mid,arr)
    def merge(self,left,right,mid,arr):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        arr[left:right+1] = temp
        print(arr)
# # 6、堆排序 - 
# import heapq
# class Solution:            
#     def Sort(self,arr):
#         if not arr: return []
#         heap = heapq.heapify(arr)
#         print([heapq.heappop(arr) for _ in range(len(arr))])
# 6、堆排序 - 手动维护堆
class Solution:            
    def Sort(self,nums):
        for i in range((len(nums)-2)//2, -1, -1):
            self.heapify(i, len(nums), nums)
        for j in range(len(nums)-1, 0, -1):
            nums[j], nums[0] = nums[0], nums[j]
            self.heapify(0, j, nums)
        print(nums)
    def heapify(self,parent_index, length, nums):
        temp = nums[parent_index]
        child_index = 2*parent_index+1
        while child_index < length:
            if child_index+1 < length and nums[child_index+1] > nums[child_index]:
                child_index = child_index+1
            if temp > nums[child_index]:
                break
            nums[parent_index] = nums[child_index]
            parent_index = child_index
            child_index = 2*parent_index + 1
        nums[parent_index] = temp

# 初级排序+堆排序测试
Solution().Sort([])
Solution().Sort([2, 8, 7, 4, 6, 3,6])
Solution().Sort([12,4,132,55,46,232,789,1,0,98,523,666])
# 快排/归并测试
# Solution().Sort(0,0,[])
# Solution().Sort(0,6,[2, 8, 7, 4, 6, 3,6])
# Solution().Sort(0,11,[12,4,132,55,46,232,789,1,0,98,523,666])