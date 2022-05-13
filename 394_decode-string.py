class Solution1: #递归法
    def decodeString(self, s: str) -> str:
        return self.dfs(s,0)

    def dfs(self, s: str,i) -> str:
        # 从左到右遍历，左括号之前是K，左括号到右括号之间是content,rs=k*content
        # 遇到多次括号用递归
        k = '' #倍数的变量
        content = '' #用来存储计算结果的字符串
        while i < len(s):
            print('***',s,content,i)
            if s[i].isdigit(): #数字字符存储到k,作为倍数
                k += s[i]
            elif s[i] == '[': #遍历到左括号时，开启新一轮递归。递归的字符串从左括号的下一个字符开始，直到改左括号对应的右括号结束
                i,temp = self.dfs(s,i+1) # 递归时，返回值有两个，一个是遍历结束的索引值，一个是递归拼接的结果值
                content += int(k)*temp # 解码结果=递归拼接的结果值*倍数
                k = ''# 重置倍数的变量
                # i跳过了递归区间，i+1可能是"]",也可能是数字
            elif s[i] == ']':# 遍历到]表示一个编码区间减速，直接返回结果值，跳出递归
                return i,content
            else:
                content += s[i]
            i+=1
        return content

class Solution: #迭代法、辅助栈
    def decodeString(self, s: str) -> str:
        return self.dfs(s,0)

    def dfs(self, s: str,i) -> str:
        # 从左到右遍历，左括号之前是K，左括号到右括号之间是content,rs=k*content
        # 只遍历一遍，时间复杂度O（n）,空间复杂度和栈的缓存相关，最多为O（n）
        k = '' #倍数的变量
        content = '' #用来存储计算结果的字符串
        stack=[]
        while i < len(s):
            # print('***',s,content,i)
            if s[i].isdigit(): #数字字符存储到k,作为倍数
                k += s[i]
            elif s[i] == '[': # 入栈
                stack.append((k,content))
                k = ''# 重置倍数的变量
                content = ''
                # i跳过了递归区间，i+1可能是"]",也可能是数字
            elif s[i] == ']':# 出栈
                temp = content
                k,content = stack.pop()
                # print('***',k,temp,content,i)
                content += int(k)*temp
                k = ''# 错误点：重置倍数的变量，后面可能还有
            else:
                content += s[i]
            i+=1
        return content

# print(Solution().decodeString("3[a]2[bc]"))
# print(Solution().decodeString("3[a2[c]]"))