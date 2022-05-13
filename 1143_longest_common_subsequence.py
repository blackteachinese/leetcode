class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # method1: dynamic programming
        # 两个序列，需要用二维数组表示两个状态dp[i][j]
        # 符合无后效性
        # dp[i][j]是指长度为i-1的text1和长度为j-1的text2的最长公共子序列的长度。
        # 二维数组dp[i][j]可以递推为dp[i][j-1],dp[i-1][j-1],dp[i-1][j]
        # dp[i][j] = dp[i-1][j-1] if text1[i] == test2[j]
        # dp[i][j] = max(dp[i-1][j],dp[i][j-1]) if text1[i] != test2[j]
        # 初始值：dp[0][0] = 0,dp[1][0] = 0,dp[0][1] = 0
        m,n=len(text1),len(text2)
        if m < 1 or n < 1 : return 0
        i=j=1
        dp = [[0]* (n+1) for _ in range(0,m+1)]
        dp[0][0] = dp[1][0] = dp[0][1] = 0
        # while j + 1 < n:  
        # ！！！！ 要双层循环遍历才能比较所有字母的情况
        # 因为i和j从1开始遍历，text1要从i-1开始取才是第一个，text2要从j-1开始取才是第一个
        # 因此，要遍历完text1，range需要到m+1，要遍历完text2，range需要到n+1
        for i in range(1,m+1):
            for j in range(1,n+1):
                # print(i,j,text1[i-1],text2[j-1])
                # !!!!!! 必须保证text1和text2的每个字符都要比较过
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        # print(dp)
        return dp[m][n]


# print(Solution().longestCommonSubsequence("abcde","ace"))