class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 双指针i1,i2，分布从字符串尾部开始遍历
        # 从个位数开始计算，结果存储在rs,进位缓存到temp
        # 遍历到i1和i2都为0结束
        # 时间复杂度O(max(n,m)),空间复杂度O(max(n,m))
        i1,i2,temp=len(num1)-1,len(num2)-1,0
        res =''
        while i1 >= 0 or i2 >= 0:
            n1=int(num1[i1] if i1 >= 0 else 0)
            n2=int(num2[i2] if i2 >=0 else 0)
            sum = n1+n2+temp
            temp = 1 if sum >= 10 else 0
            res = str(sum%10) + res
            # print(temp,res)
            i1 = i1 - 1
            i2 = i2 - 1
        if temp > 0: # 错误点：漏掉最后的进位值
            res = str(temp) + res
        return res
# print(Solution().addStrings('11','123'))
# print(Solution().addStrings('0','0'))
# print(Solution().addStrings('456','77'))
# print(Solution().addStrings('1','9'))
