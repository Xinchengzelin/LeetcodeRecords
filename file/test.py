# 归并排序
class Solution:
    def Sort(self,begin,end,arr):
        if begin >= end:
            return
        mid = (begin + end) >> 1
        self.Sort(begin,mid,arr)
        self.Sort(mid+1,end,arr)
        self.merge(begin,end,mid,arr)
        print(arr)

    def merge(self,begin,end,mid,arr):
        temp = []
        i,j = begin, mid+1
        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        if i <= mid:
            temp.extend(arr[i:mid+1])
        if j <= end:
            temp.extend(arr[j:end+1])
        arr[begin:end+1] = temp
        print(temp)

Solution().Sort(0,0,[])
Solution().Sort(0,6,[2, 8, 7, 4, 6, 3,6])
Solution().Sort(0,11,[12,4,132,55,46,232,789,1,0,98,523,666])