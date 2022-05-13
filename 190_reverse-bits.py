from operator import index
from textwrap import indent

# method1: 逐位颠倒 >> move to right
class Solution:
    def reverseBits(self, n: int) -> int:
        index = 31
        rs=0
        while index >= 0:
            lastBit = n & 1 # 取当前最后一位的bit值
            # print(n,lastBit,n >> 1,lastBit << index)
            rs = rs | (lastBit << index) # 左移相应的位数，实现该位颠倒
            n = n >> 1  # 右移去掉最后一位
            index -= 1
        return rs

# method2: 位运算分治
class Solution:
    def reverseBits(self, n: int) -> int:
        # 1 dividing into two groups  
        # 2 change position of two groups  
        # 3 reverse two group 
        # 4 recurve to dividing the group until every group is two bits
        # 注意加括号，控制作用域
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) # 每16位一组进行互换，前8位都右移动8位，后8位都左移8位
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4) # 每8位一组进行互换，前4位都右移动4位，后4位都左移4位
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2) # 每4位一组进行互换，前2位都右移动2位，后2位都左移2位
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1) # 每2位一组进行互换，前1位都右移动1位，后1位都左移1位
        return n

print(Solution().reverseBits(43261596))