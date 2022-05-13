class Solution:
     # Approach 1: brute force  O(n)
    # Approach 2: bit move to right
    def myPow1(self, x: float, n: int) -> float:
        # Approach 3: 快速幂 + 递归 容易 x*x = x^2, x^2*x^2 = X^4
        # if n is even number x^n = x^(n/2)*x^(n/2)
        # elif n is odd number x^n = x^(n/2)*x^(n/2)*x
        # when n is negative number , x^n =  (1/x) ^(-n)
        # O(logn) 每次递归指数n减少一半
        def quickmul(t: int) -> float:
            if t == 0: # 递归的边界为 n = 0n=0，任意数的 00 次方均为 1
                return 1.0 # 错误点：t == 0 时 return 1.0 而不是x
            y= quickmul(t // 2)
            return y*y if t % 2 == 0 else y*y*x
        return quickmul(n) if n >= 0 else 1 / quickmul(-n)

    def myPow(self, x: float, n: int) -> float:
       
        # Approach 4: 快速幂 + 迭代 难理解 尽量别写，看题解
       
        
        if n == 0 : return 1
        res = 1.0
        if n < 0:
            x = 1 / x
            n = -n
        while n > 0:
            if n % 2 == 1:
                res=res*x # x要累计乘积
            res=res*res
            n = n // 2
        return res
