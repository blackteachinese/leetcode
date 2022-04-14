from functools import cmp_to_key
from typing import List


class Solution1:
    def minNumber(self, nums: List[int]) -> str:
        # method1:排序，从小到大拼接？
        # 注意：30需要排在3前面，因此需要定制判断逻辑
        # nums.sort(key=cmp_to_key(lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))))
        res=sorted(nums,key=cmp_to_key(lambda x,y: int(str(x) + str(y)) - int(str(y) + str(x))))
        return "".join(map(str,res))
        # return "".join(str(x) for x in res)

class Solution2:
    def minNumber(self, nums: List[int]) -> str:
        # method1:排序，从小到大拼接？
        # 注意：30需要排在3前面，因此需要定制判断逻辑
        def compare(x,y):
            a,b = x+y,y+x
            if a < b:
                return -1 # first argument is small
            elif a < b:
                return 1 # first argument is greater than the second argument
            else:
                return 0 # first argument is equal to the second argument
        strs=[str(num) for num in nums]
        res=sorted(strs,key=cmp_to_key(compare))
        return "".join(map(str,res))

# offer45
class Solution3: # 快速排序，取l所在的值作为flag
    def minNumber(self, nums: List[int]) -> str:
        # 注意：30需要排在3前面，因此需要定制判断逻辑
        def quicksort(l,r):
            if l >= r: return
            i,j,flag=l,r,strs[l] # 取l所在的值作为flag
            while i < j :
# 错误点：因为取l所在的值作为flag，所以要先判断右边。j的判断逻辑要放在i的前面，反之
                while strs[j] + flag >= flag + strs[j] and i < j: 
                    j-=1
                while strs[i] + flag <= flag + strs[i] and i < j: # 错误点：漏掉=号，元素相等时会错误
                    i+=1
                print(i,j,flag,strs)
                strs[i],strs[j]=strs[j],strs[i]
            strs[l],strs[i]=strs[i],strs[l] #错误点：每次循环后，都要将flag替换到中间点，确保flag左边都比flag小，反之
            # 左边到i-1,右边从i+1开始。i的位置已经是排序后的正确位置，不用再处理，
            quicksort(l,i-1) 
            quicksort(i+1,r)
        strs=[str(num) for num in nums]
        quicksort(0,len(strs) - 1)
        return "".join(map(str,strs))

class Solution: # 快速排序，取r所在的值作为flag
    def minNumber(self, nums: List[int]) -> str:
        def quicksort(l,r):
            if l >= r: return
            i,j,flag=l,r,strs[r] # 取r所在的值作为flag
            while i < j :
                # 取r所在的值作为flag，所以要先判断左边。i的判断逻辑要放在j的前面，
                while strs[i] + flag <= flag + strs[i] and i < j: 
                    i+=1
                while strs[j] + flag >= flag + strs[j] and i < j: 
                    j-=1
                print(i,j,flag,strs)
                strs[i],strs[j]=strs[j],strs[i]
            strs[r],strs[i]=strs[i],strs[r] 
            quicksort(l,i-1)
            quicksort(i+1,r)
        strs=[str(num) for num in nums]
        quicksort(0,len(strs) - 1)
        return "".join(map(str,strs))


print(Solution().minNumber([10,2]))
print(Solution().minNumber([1,1,1]))
print(Solution().minNumber([5,30,34,2,9]))
print(Solution().minNumber([3,30,34,5,9,10]))
print(Solution().minNumber([3,30,34,5,9]))



