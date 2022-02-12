class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        self.numRows = numRows
        self.isDown = True
        array = ['']*numRows
        # print(numRows,array)
        index = 0
        column = None
        while index < len(s):
            column = self.getNextPosition(column)
            # print(column,array)
            array[column] += s[index]
            index += 1
        return ''.join(array)
        
    def getNextPosition(self,column: int) -> int:
        if column == None:
            return 0
        # 向下
        if self.isDown and column + 1 < self.numRows:
            column += 1
            if column == self.numRows - 1:
                self.isDown = False
        elif column- 1 >= 0:
        # Z型向上
            column -= 1
            if column == 0:
                self.isDown = True
        return column


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            print(i,flag)
            i += flag
        return "".join(res)

    def convert1(self, s: str, numRows: int) -> str:
        array = ['']*numRows
        column,flag = 0,-1 #设置flag默认值-1，是为了后面if逻辑简单一点
        for c in s:
            # print(column,array)
            array[column] += c
            if column == numRows - 1 or column == 0 : flag *= -1
            column += flag
        return ''.join(array)
        


# rs=Solution().convert("PAYPALISHIRING",3)
rs=Solution().convert("AB",1)
print(rs)