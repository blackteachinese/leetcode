from typing import List


class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 方法1：暴力/双指针：遍历数组?，对比相邻两个子数组，比较尾数和头数，用新数组res归档
        # 如果不能合并，归档第一个数组；
        # 如果可以合并，合并后存到left,将right从数组中移除，j从新回到i+1，再继续遍历
        # time O(n^2)
        # 边界
        if len(intervals) < 2:
            return intervals
        # main
        res=[]
        merge = None
        right = None
        i=0
        while i < len(intervals):
            left = intervals[i]
            j = i+1
            while j < len(intervals):
                right=intervals[j]
                if left[1] >= right[0] and left[0] <= right[1]: #可以合并
                    left = [min(left[0],right[0]),max(right[1],left[1])]
                    intervals.pop(j)
                    j=i+1 # 继续从头遍历
                    continue
                j+=1
            i+=1
            res.append(left)
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #方法2：先排序，排序后只需要遍历一次，而且只需要比价left[1]和right[0]的关系
        #time O(nlogn)
        intervals.sort()
        i=0
        while i+1 < len(intervals):
            left=intervals[i]
            right=intervals[i+1]
            if left[1] >= right[0]: # merge
                left = [left[0],max(left[1],right[1])]
                intervals[i] = left
                intervals.pop(i+1)
            else:
                i+=1
        return intervals


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[1,3]]))
print(Solution().merge([[1,4],[0,4]])) # 遗漏的case
print(Solution().merge([[3,6],[0,3]])) # 遗漏的case
print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]])) # 遗漏的case