
import heapq
from typing import List 

class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # ** 暴力破解法：O(n^2)
        # 1快速排序，取第K个数 O(logn) 
        # *** 快排 时间是O(n) 空间是O（1）
        # 2建一个元素个数为K的最小堆，去最小的元素 O(logn)?
        # 分析：3min
        # coding 12min
        # 边界处理 不需要1 <= k <= nums.length <= 104
        # 建堆
        # *** 建立最小堆，遍历数据O(N),堆内元素跳转O(logK),总时间为O(NlogK)，空间是O(k)
        rs = heapq.nlargest(k,nums)
        return rs[len(rs) - 1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # ** 暴力破解法：O(n^2)
        # 1快速排序，取第K个数 O(logn) 
        # *** 快排 时间是O(n) 空间是O（1）
        self.fastsort(nums,0,len(nums) - 1)
        print(nums)
        return nums[k - 1]
    def fastsort(self,q:List[int],l:int,r:int):
        # 快排、降序
        # 退出条件
        if l >= r:
            return
        # 1 确定分界点
        mid = int((l + r) / 2)
        midV = q[mid]
        i,j = l,r
        # 2 区间内排序
        while i < j:
            while q[i] > midV:
                i += 1
            while q[j] <= midV and j > 0:
                j -= 1
                print(i,j,mid,midV,q)
            if i < j:
                q[i],q[j] = q[j],q[i]
        # 3 递归处理左右两个区间
        self.fastsort(q,l,j)
        self.fastsort(q,j+1,r)



    def fastsort2(self,q:List[int],l:int,r:int):
        # 快排、降序
        # 快速排序不适合解决有重复元素的数据
        # 退出条件
        if l >= r:
            return
        # 1 确定分界点
        mid = int((l + r) / 2)
        midV = q[mid]
        i,j = l,r
        # print(l,r,(l + r) / 2,midV)
        # 2 区间内排序
        index = -1
        while i < j:
            # print(i,j,mid,midV,q)
            while q[i] > midV:
                i += 1
            while q[j] < midV:
                j -= 1
            if i < j:
                q[i],q[j] = q[j],q[i]
            if q[i] == midV and i == mid:
                print(i,j,mid,midV,q)
                j -= 1
                # index = i
                # print(i,j,mid,midV,q)
                # break
            # if q[j] == midV and j == mid:
            #     print(i,j,mid,midV,q)
            #     i += 1
                # index = j
                # break
        if index == -1:
            index = j
        # 3 递归处理左右两个区间
        self.fastsort(q,l,index)
        self.fastsort(q,index+1,r)


print(Solution().findKthLargest([3,2,1,5,6,4],2))
# print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4))