class Solution:
    def reverse(self, x: int) -> int:
        rever =[]
        source = x
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if x < 0:
            source *= -1
        while source > 0:
            rever.append(source%10)
            source = int(source/10)
        rs = 0
        times = 1
        while len(rever):
            rs += rever.pop()*times
            if rs < INT_MIN or rs > INT_MAX:
                return 0
            times *= 10
        if x < 0:
            rs *= -1
       
        return rs


rs = Solution().reverse(-321)
rs = Solution().reverse(1534236469)
print(rs)