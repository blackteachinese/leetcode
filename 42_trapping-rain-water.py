from typing import List
import numpy as np
class Solution1:
    def trap(self, height: List[int]) -> int:
        # 双指针
        l,b,r,flag,result=0,0,1,False,0
        lastStack=[]
        # l先指向0,r向右遍历
        # 如果r<l,标记为可蓄水状态flag=1
        # 当flag=0，如果r>=l,l移动到r的位置
        # 当flag=1，如果r>=l,达成蓄水条件,计算l到r的蓄水量。然后开始找下一个区域，l移动到r的位置，flag=0
        # 需水量 =  (r-l-1)* min(l,r) - "List[l+1:r-1]之和"
        # 有嵌套，要用栈
        while r < len(height):
            print(l,b,r,flag,height[l],height[b],height[r],lastStack,result)
            if height[r] < height[b]:
                if flag == False :
                    flag = True
                    b+=1
                else:
                    # 内嵌区间
                    lastStack.append((l,b))
                    l+=1
                    b+=1
            elif height[r] > height[b]:
                if flag == False :
                    l+=1
                    b+=1
                    # 如果还有更高的左柱，取出来
                    # if len(lastStack) > 0:
                    #     l,b = lastStack.pop()
                    #     continue
                else:
                    hmin = height[b]
                    hmax = min(height[l],height[r])
                    w=(r-l-1)
                    result+=w*(hmax-hmin)
                    #result += (r-l-1)*min(l,r) - np.sum(height[l+1:r-1])
                    if len(lastStack) > 0:
                        l,b = lastStack.pop()
                        r+=1
                        continue
                    l=b=r
                    flag=False
            r+=1
        # print(l,r)
        return result


class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针
        l,r,flag,result=0,1,False,0
        lastStack=[]
        top=height[0]
        eatTop=0
        tempCount=0
        # l先指向0,r向右遍历
        # 如果r<l,标记为可蓄水状态flag=1
        # 当flag=0，如果r>=l,l移动到r的位置
        # 当flag=1，如果r>=l,达成蓄水条件,计算l到r的蓄水量。然后开始找下一个区域，l移动到r的位置，flag=0
        # 需水量 =  (r-l-1)* min(l,r) - "List[l+1:r-1]之和"
        # 有嵌套，要用栈
        while r < len(height):
            print(l,r,flag,height[l],height[r],lastStack,result)
            if height[r] < height[l]:
                if flag == False :
                    flag = True
                else:
                    # 内嵌区间
                    lastStack.append((l,b))
                    l+=1
            elif height[r] > height[b]:
                if flag == False :
                    l+=1
                    b+=1
                    # 如果还有更高的左柱，取出来
                    # if len(lastStack) > 0:
                    #     l,b = lastStack.pop()
                    #     continue
                else:
                    # hmin = height[b]
                    # hmax = min(height[l],height[r])
                    # w=(r-l-1)
                    # result+=w*(hmax-hmin)
                    count = (r-l-1)*min(height(l),height(r)) - np.sum(height[l+1:r-1])
                    # 如果r是最高的,重新初始化
                    if height[r] > top:
                        result += count
                        top = height[r]
                    else: # 如果r不是最高，
                        # 暂时缓存洼地的值
                        eatTop=min(height(l),height(r))
                        
                    l=b=r
                    flag=False
                  
            r+=1
        # print(l,r)
        return result


# print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,0,3,2,5]))