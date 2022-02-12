class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 特殊值:只有一个字母也是回文
        if len(s) < 2:
            return s
        # 初始化dp数组
        dp = [[False]*len(s) for _ in range(len(s))]
        # 递推公式：dp[i][j] = d[i+1][j-1] and (s[i] == s[j])
        # 初始：单个字母或一对字母作为开始
        longest = s[0:1]
        for j in range(0,len(s)):
            for i in range(0,j): # i是左边界，j是右边界，i必须小于j
                if s[i] != s[j]: # 第一步：如果左右边界不相等，肯定不是回文
                    dp[i][j] = False
                    continue
                elif j - i <= 2:  # 第二步：已知边界值相等，去掉两个边界值，如果只剩一个是回文（例如：9-7=2 中间只有一个值）
                    print("==",i,j,dp[i+1][j-1])
                    dp[i][j] = True
                    print(dp)
                else:  # 第三步：已知边界值相等，去掉两个边界值，如果剩下的字符串是回文那加上边界值也是回文，反之
                    print("==",i,j,dp[i+1][j-1])
                    print(dp)
                    dp[i][j] = dp[i+1][j-1]
                # 如果i到j之间是回文，判断是不是当前的最长回文，如果是就存下来
                temp = s[i:j+1]
                print(i,j,temp,dp[i][j])
                if dp[i][j] == True and len(temp) > len(longest):
                    longest = temp
        # print(dp)
        return longest 


# rs=Solution().longestPalindrome("babad")
# rs=Solution().longestPalindrome("ac")
# rs=Solution().longestPalindrome("aacabdkacaa")
rs=Solution().longestPalindrome("abcba")
print(rs)