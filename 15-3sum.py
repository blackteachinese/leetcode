class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: brute force O(n^3)
        # Approach 2: brute force + hashmap O(n^2) wrong 不重复！！！
        # Approach 3: sort + two pointer +a<=b<=c  O(n^2) 不重复！！！
        # 当我们需要枚举数组中的两个元素时，如果我们发现随着第一个元素的递增，第二个元素是递减的，那么就可以使用双指针的方法
        nums.sort()
        n=len(nums)
        res=[]
        for a in range(0,n):
            l = a+1
            r = n-1
            # skip the same element, when the second time meet the element
            # !!! we can not skip the same element when we meet the element at the frst time
            if a > 0 and nums[a] == nums[a-1]:
                continue
            while l < r:
                sum = nums[a] + nums[l] + nums[r]
                if sum ==0 :
                    # bingo
                    res.append([nums[a],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    # strip duplicate element
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
                    while l < r and nums[r+1] == nums[r]:
                        r -=1   
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return res
        # Approach 4: sort + two pointer + hash ???