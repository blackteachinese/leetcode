from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #方法1：遍历数组，if nums[i] > nums[i+1],i是峰值。时间O(n)
        #方法2：双指针，同时从前后两个方向遍历。时间O(n/2)
        #方法3：二分法，
        # 因为nums[-1] = nums[n] = -∞，所有至少有一个峰值
        # 两种情况只有一个峰值，当且数组是升序序列时，最后一位是峰值；当数组是降序序列时，第一位是峰值
        # 根据以上条件可推导：降序的左边一定有峰值，升序的右边一定有峰值

        def get(i : int) -> int:
            # 重要！！！：左右边界值统一处理，简化判断逻辑
            if i == -1 or i == len(nums): 
                return float('-inf')
            return nums[i]

        def arrange(nums,l,r): #递归写法
            # 简化边界
            # if l + 1 == len(nums):
            #     return l
            # elif r == 0:
            #     return r
            m = l + int((r - l)/2)
            # 判断
            if get(m -1) < get(m) > get(m + 1) :
                return m
            elif get(m) > get(m + 1): # 降序,左边一定有峰值，放弃右边
                return arrange(nums,l,m)
            else:   # 升序的右边一定有峰值,放弃左边
                return arrange(nums,m+1,r)
        return arrange(nums,0,len(nums) -1)

class Solution1: # 三处错误点
    def findPeakElement(self, nums: List[int]) -> int:
        # 迭代写法
        def get(i : int ) -> int:
            print('i:',i)
            if i == -1 or i == len(nums):
                return float('-inf')
            else:
                return nums[i]
        # l,r = 0,len(nums)
        l,r = 0,len(nums) - 1 #错误点：r初始化没-1
        ans = -1
        while l <= r: #错误点：少了等号
            m = (r + l)//2
            print('m',m)
            if get(m-1)< get(m) > get(m+1):
                ans= m
                break # 错误的：忘记break
            if get(m)<get(m+1):
                l = m+1
            else:
                r = m-1
        print(l,r,ans)
        return ans


# print(Solution().findPeakElement([1,3,2,1]))
print(Solution().findPeakElement([1,2]))
# print(Solution().findPeakElement([2,1]))
# print(Solution().findPeakElement([1,2,1,3,5,6,4]))
# print(Solution().findPeakElement([1,2,3,1]))
# print(Solution().findPeakElement([1,2,1,3,5,6,7]))
# print(Solution().findPeakElement([5,4,3,2]))