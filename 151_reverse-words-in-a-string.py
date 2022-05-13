class Solution1:
    def reverseWords(self, s: str) -> str:
        # 思路：自己
        # strip掉头尾空格
        s = s.strip()
        # 分割字符串，过滤中间有多个空格的情况，输出数组
        list1 = []
        tempStr = ''
        s = s + ' '
        for character in s:
            if character == ' ':
                if len(tempStr) > 0:
                    list1.append(tempStr)
                    tempStr = ''
                continue
            else:
                tempStr = tempStr + character
        # reverse数组
        list1.reverse()
        # 以空格为分隔符，拼接reverse后的数组
        rs = list1[0]
        for i in range(1,len(list1)):
            obj = list1[i].strip(' ')
            rs = rs + ' ' + obj
        return rs

        # return " ".join(reversed(s.split()))

class Solution2:
    def reverseWords(self, s: str) -> str:
        # 思路：参考题解优化
        # split分割字符串，中间有多个空格也会过滤掉
        list1 = s.split()
        print(list1)
        # reverse数组
        # 以空格为分隔符，拼接reverse后的数组
        return ' '.join(list1.reverse())

class Solution:
    def reverseWords(self, s: str) -> str:
        # 思路：参考题解优化
        # split分割字符串，中间有多个空格也会过滤掉
        # reverse数组
        # 以空格为分隔符，拼接reverse后的数组
        return ' '.join(reversed(s.split()))

class Solution:
    def reverseWords(self, s: str) -> str:
        # 思路：双端队列，利用双端队列，每次都从头部插入单词，插入之后相当于就是reverse了