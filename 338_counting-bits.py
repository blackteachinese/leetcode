from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Approach 1 : 
        # enumrate 0,n ;  O(n) 
        # x & x - 1 until x equal 0; O(logn)
        # Approach 2 : 
        # 令 y=x~\&~(x-1)y=x & (x−1)，则 yy 为将 xx 的最低设置位从 11 变成 00 之后的数，显然 0 \le y<x0≤y<x，\textit{bits}[x]=\textit{bits}[y]+1bits[x]=bits[y]+1。因此对任意正整数 xx，都有 \textit{bits}[x]=\textit{bits}[x~\&~(x-1)]+1bits[x]=bits[x & (x−1)]+1
        bits = [0] # 递推初始值，x == 0 时，二进制位为1也为0
        for x in range(1, n+1): # 错误点：x需要从1开始到n+1
            bits.append(bits[x & (x - 1)] + 1)
            print(x,x & (x - 1),bits[x])
        return bits

print(Solution().countBits(4))